import io
import itertools
import logging
import os
import sys

import pandas as pd
import requests

# from webp import WebP
from google.cloud import storage
from PIL import Image
from progress import Progressbar
from utils.utils import read_yaml, send_data2api

# request timeout
TIMEOUT = 60

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")
AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME")
print(f"AIRFLOW_HOME: {AIRFLOW_HOME}")
KEYWORD, SITE, SCRAPED_TIME, N_IMGS = sys.argv[1:]
N_IMGS = int(N_IMGS)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = f"{AIRFLOW_HOME}/m2-key.json"

secret = read_yaml(AIRFLOW_HOME)


class PixabayCrawler:
    def __init__(self, key_words, params, bucket):
        self.keywords = key_words
        self.params = params
        self.bucket = bucket

    def get_json(self):
        try:
            url = f"https://pixabay.com/api/?key={self.params['key']}"
            for k, v in self.params.items():
                if k != "key":
                    url += f"&{k}={v}"
            r = requests.get(url, allow_redirects=False, timeout=TIMEOUT)
            logging.debug(f"json url - {r.url}")
        except requests.exceptions.Timeout as err:
            logger.warning(err)

        try:
            return r
        except Exception as err:
            logger.warning(err)

    def download_img(self, url):
        try:
            r = requests.get(url, allow_redirects=False, timeout=TIMEOUT)
            logging.debug(f"image url - {r.url}")
        except requests.exceptions.Timeout as err:
            logger.warning(err)

        try:
            return r.content
        except Exception as err:
            logger.warning(err)

    def get_available_images(self):
        self.params["page"] = 1
        # self.params["per_page"] = MIN_IMG_PER_PAGE
        j_response = self.get_json().json()
        return j_response["total"]

    def scraper(self, n_imgs=1):
        logger.debug((self, self.keywords, n_imgs))
        # go to https://pixabay.com/api/docs/ to look up these values

        # path = Path(path)
        df = pd.DataFrame(
            columns=[
                "tag",
                "img_path",
                "img_width",
                "img_height",
                "crawled_time",
                "label",
            ]
        )
        logger.info("Starting")
        n_imgs2gcs = 0
        for keyword in self.keywords:
            try:
                self.params["q"] = keyword
                print(f"Now searching for '{keyword}'")
                # testing if pixabay can serve the amount of wanted images
                n_imgs = self.test_if_pixabay_can_serve(n_imgs)

                Pbar = Progressbar(n_imgs)

                # creating the params list for all pages
                imgs_progress = 0

                run = True

                for page in itertools.count(1):
                    try:
                        if not run:
                            break

                        self.params["page"] = page
                        j_response = self.get_json().json()

                        for img_dict in j_response["hits"]:
                            try:
                                if imgs_progress >= n_imgs:
                                    run = False
                                    break
                                if self.is_valid(img_dict["id"]):
                                    self.send_img2gcs(img_dict)
                                    df = self.append_df(df, img_dict)
                                    n_imgs2gcs += 1

                                imgs_progress += 1
                                Pbar.set(imgs_progress)

                            except Exception as err:
                                logger.warning(err)
                                logger.warning(
                                    f"an error occured proccesing this images {img_dict['largeImageURL']}"
                                )

                    except Exception as err:
                        logger.warning(err)
                        logger.warning(f"an error occured proccesing page {page}")
                        logger.warning(
                            f"downloaded {imgs_progress} images from {keyword}"
                        )
                        break
            except Exception as err:
                logger.warning(err)
                logger.warning(f"an error occured proccesing the class {keyword}")
        return df, n_imgs2gcs

    def append_df(self, df: pd.DataFrame, img_dict: dict) -> pd.DataFrame:
        """append new dataframe to the old one

        Args:
            df (pd.DataFrame): dataframe
            img_dict (dict): img_dict from pixabay api

        Returns:
            pd.DataFrame: new dataframe with old dataframe
        """ """"""
        df = pd.concat(
            [
                pd.DataFrame(
                    [
                        [
                            img_dict["tags"],
                            f"{KEYWORD}/{SITE}/{SCRAPED_TIME}/{img_dict['id']}.webp",
                            img_dict["webformatWidth"],
                            img_dict["webformatHeight"],
                            SCRAPED_TIME,
                            "NaN",
                        ]
                    ],
                    columns=df.columns,
                ),
                df,
            ],
            ignore_index=True,
        )

        return df

    def test_if_pixabay_can_serve(self, n_imgs: int) -> int:
        """test if pixabay can serve the amount of wanted images

        Args:
            n_imgs (int): the amount of wanted images

        Returns:
            int: the amount of wanted images
        """
        available_imgs = self.get_available_images()
        print(f"There are {available_imgs} available images...")
        if available_imgs < n_imgs:
            logger.info(
                f"There are only {available_imgs} available images... starting download"
            )
            n_imgs = available_imgs - 1
        return n_imgs

    def is_valid(self, img_id: int) -> bool:
        """check img_id is a duplicate

        Args:
            img_id (str): img id of pixabay

        Returns:
            bool: True if not duplicate
        """
        url = f"{secret['api_url']}/api/v1/meta/duplicate_check"
        data = {"id": str(img_id), "category": KEYWORD}

        try:
            res = requests.post(url, json=data)
            res.raise_for_status()
            return res.json()["valid"]
        except Exception as err:
            logger.warning(err)
            logger.warning("an error occured requesting duplicate check")

    def send_img2gcs(self, img_dict: dict) -> None:
        """send img to gcs

        Args:
            img_dict (dict): img_dict from pixabay api
        """
        file_name = f"{KEYWORD}/{SITE}/{SCRAPED_TIME}/{str(img_dict['id'])}.webp"
        img_bytes = self.download_img(img_dict["webformatURL"])
        img_PIL = Image.open(io.BytesIO(img_bytes))
        webp_io = io.BytesIO()
        img_PIL.save(webp_io, format="WEBP", quality=80)
        try:
            blob = self.bucket.blob(file_name)
            blob.upload_from_string(webp_io.getvalue(), content_type="image/webp")
        except Exception as err:
            logger.warning(err)
            logger.warning(
                f"an error occured saving this images {img_dict['largeImageURL']}"
            )


if __name__ == "__main__":
    category = [
        "animals",
        "backgrounds",
        "fashion",
        "nature",
        "science",
        "education",
        "feelings",
        "health",
        "people",
        "religion",
        "places",
        "industry",
        "computer",
        "food",
        "sports",
        "transportation",
        "travel",
        "buildings",
        "business",
        "music",
    ]

    MAX_IMG_PER_PAGE = 200
    MIN_IMG_PER_PAGE = 3

    params = {
        "key": secret["pixabay_api"],
        "q": "None",
        "image_type": "photo",
        "page": 1,  # Returned search results are paginated. Use this parameter to select the page number.
        "per_page": 20,  # Determine the number of results per page. Accepted values: 3 - 200. Default: 20.
        "category": "None",
        "safesearch": "true",
        "order": "latest",
    }

    storage_client = storage.Client()
    bucket_name = "scraped-img"
    bucket = storage_client.bucket(bucket_name)

    if KEYWORD == "animal":
        keyword = [KEYWORD, "Mammal"]
        params["category"] = category[0]
    elif KEYWORD == "landmark":
        keyword = [KEYWORD, "Unesco", "tourist attraction"]
        params["category"] = category[10]
    scraper = PixabayCrawler(keyword, params, bucket)
    df, n_imgs2gcs = scraper.scraper(n_imgs=N_IMGS)
    print(f"Number of img2gcs is {n_imgs2gcs}")
    # send_metadata2api(df)
    send_data2api(logger, KEYWORD, secret, df, "create")
    # TODO: 이전에 크롤링했던 사진 이후부터 크롤링
    # TODO: pixabay에서 url전부 뽑고 url리스트를 api에 전달해서 한번에 중복체크, 그 후 멀티프로세싱이나 비동기로 이미지 다운
