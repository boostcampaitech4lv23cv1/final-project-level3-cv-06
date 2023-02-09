import os
import sys

import pandas as pd
import pyarrow as pa
import pyarrow.feather as feather
import requests
import yaml
from geopy.geocoders import Nominatim
from google.cloud import storage, vision
from infer_animal import make_duration_list
from PaintTransformer.inference import inference, init
from PIL import Image
from tqdm import tqdm

AIRFLOW_HOME = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
)
KEYWORD, SITE, SCRAPED_TIME = sys.argv[1:]

with open(f"{AIRFLOW_HOME}/secret.yml", "r") as f:
    secret = yaml.load(f, Loader=yaml.FullLoader)

os.environ["GCLOUD_PROJECT"] = "CV-NOOPS"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = f"{AIRFLOW_HOME}/m2-key.json"


def get_country(latitude: int, longitude: int, cc_df: pd.DataFrame) -> str:
    """get country from latitude and longitude

    Args:
        latitude (int): latitude
        longitude (int): longitude
        cc_df (pd.DataFrame): country code dataframe
    Returns:
        str: country
    """
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse(
        f"{latitude}, {longitude}", exactly_one=True, language="en"
    )
    try:
        country_code = location.raw["address"]["country_code"].upper()
        return cc_df[cc_df["code"] == country_code]["korean"].values[0]
    except Exception:
        return "NaN"


def get_country_landmark_gcs(
    bucket_name: str, file_names: list, cc_df: pd.DataFrame
) -> list:
    """get country from gcs landmarks images

    Args:
        bucket_name (str): bucket name
        file_names (list): gcs file names
        cc_df (pd.DataFrame): country code dataframe
    Returns:
        list: countries
    """
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    countries = []
    print(f"The number of files to be processed: {len(file_names)}")
    for file_name in tqdm(file_names):
        image.source.image_uri = f"gs://{bucket_name}/{file_name}"

        response = client.landmark_detection(image=image)
        if response.error.message:
            print(f"Error: {response.error.message}")
            continue

        if landmarks := response.landmark_annotations:
            latitude = landmarks[0].locations[0].lat_lng.latitude
            longitude = landmarks[0].locations[0].lat_lng.longitude
            country = get_country(latitude, longitude, cc_df)
            countries.append(country)
        else:
            countries.append("NaN")
    return countries


def make_df(SCRAPED_TIME, file_names, countries):
    df = pd.DataFrame(
        {
            "tag": "landmark",
            "img_path": file_names,
            "img_width": 0,
            "img_height": 0,
            "crawled_time": SCRAPED_TIME,
            "label": countries,
        }
    )
    df["use_status"] = False
    df[df["label"] != "NaN"]["use_status"] = True
    return df


def img2ani(df: pd.DataFrame) -> None:
    """convert img to animation

    1. check if img use_status is True
    2. convert img to animation using PaintTransformer
    3. save animation in webp format

    Args:
        df (pd.DataFrame): metadata dataframe
    """

    base_path = f"{AIRFLOW_HOME}/dags/classification/data/"

    resize_l = 1024
    K = 5
    stroke_num = 8
    patch_size = 32

    model, meta_brushes, device = init()

    img_paths = base_path + df["img_path"]
    print(f"img_paths: {img_paths}")
    for img_path, label in tqdm(zip(img_paths, df["label"])):
        if label != "NaN":
            save_path = img_path.split(".")[0] + "_ani.webp"
            image = Image.open(img_path)
            output = inference(
                image=image,
                resize_l=resize_l,  # resize original input to this size. (max(w, h) = resize_l)
                K=K,  # set K
                device=device,
                model=model,
                meta_brushes=meta_brushes,
                stroke_num=stroke_num,
                patch_size=patch_size,
            )
            time_consume = make_duration_list(len(output), total_time=10, mode="LINEAR")

            Image.Image.save(
                output[0],
                save_path,
                format="WEBP",
                save_all=True,
                append_images=output[1:],
                optimize=True,
                duration=time_consume,
                loop=1,
            )


def download_gcs_filter(blobs, file_names, df):
    file_list = []
    dest = f"{AIRFLOW_HOME}/dags/classification/data/"
    os.makedirs(f"{dest}{KEYWORD}/{SITE}/{SCRAPED_TIME}", exist_ok=True)
    print(f"make dir at {dest}{KEYWORD}/{SITE}/{SCRAPED_TIME}")
    all_files = {file_name: False for file_name in file_names}
    to_be_downloaded_files = df[df["label"] != "NaN"]["img_path"].to_list()
    print(f"to_be_downloaded_files: {to_be_downloaded_files}")
    for file in to_be_downloaded_files:
        all_files[file] = True
    for blob in blobs:
        if all_files[blob.name]:
            blob.download_to_filename(f"{dest}{blob.name}")
            file_list.append(f"{dest}{blob.name}")
    return file_list


def send_metadata2api(df: pd.DataFrame, KEYWORD: str) -> None:
    """send metadata dataframe to api server

    Args:
        df (pd.DataFrame): metadata dataframe
        KEYWORD (str): keyword for metadata
    """
    df = df.drop("tag", axis=1)
    url = f"{secret['api_url']}/api/v1/meta/update"

    buffer = pa.BufferOutputStream()
    feather.write_feather(df, buffer)

    file = {"file": buffer.getvalue().to_pybytes()}
    category = {"category": KEYWORD}
    res = requests.post(url, files=file, data=category)

    # Check the status code of the response
    try:
        res.raise_for_status()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    client = storage.Client()
    dir_name = f"{KEYWORD}/{SITE}/{SCRAPED_TIME}"
    bucket_name = "scraped-img"
    bucket = client.get_bucket(bucket_name)
    if blobs := list(bucket.list_blobs(prefix=dir_name)):
        file_names = [str(blob).split(",")[1].strip() for blob in blobs]
        cc_df = pd.read_csv(f"{AIRFLOW_HOME}/dags/classification/country_code.csv")
        print("Read country code csv")
        countries = get_country_landmark_gcs(bucket_name, file_names, cc_df)
        df = make_df(SCRAPED_TIME, file_names, countries)
        print("Make metadata dataframe")
        print(f"Dataframe is:\n {df}")
        file_list = download_gcs_filter(blobs, file_names, df)
        print("Start img2ani")
        img2ani(df)
        send_metadata2api(df, KEYWORD)
        print("Send metadata to api")
    else:
        print("There is no image to process")
