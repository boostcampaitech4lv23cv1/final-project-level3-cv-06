import os
import sys

import pandas as pd
import requests
import yaml

AIRFLOW_HOME = os.path.dirname(os.path.abspath(__file__))

with open(
    f"{os.path.abspath(os.path.join(AIRFLOW_HOME, '..','..'))}/secret.yml", "r"
) as f:
    secret = yaml.load(f, Loader=yaml.FullLoader)


def download_img_from_gcs(img_paths: list, paths_to_save: list):
    dest = "/opt/ml/final-project-level3-cv-06/airflow_/dags/classification/data/"
    for path_to_save in paths_to_save:
        os.makedirs(dest + "/".join(path_to_save), exist_ok=True)
    for img_path in img_paths:
        bash_script = f"gsutil -m cp gs://scraped-time/{img_path}/ {dest}{img_path}"
        os.system(bash_script)


def get_metadata_from_api() -> list:
    """get metadata from api

    Returns:
        list: metadata img_path list
    """
    url = f"{secret['api_url']}/api/v1/meta/read?category=animal"
    res = requests.get(url, allow_redirects=False)
    df = res.json()
    df = pd.DataFrame(df)
    paths_to_save = list(
        df["img_path"].str.split("/").apply(lambda x: "/".join(x[:3])).unique()
    )

    return df["img_path"].to_list(), paths_to_save


if __name__ == "__main__":
    bucket = sys.argv[1]
    img_paths, paths_to_save = get_metadata_from_api()
    download_img_from_gcs(img_paths, paths_to_save)

    # TODO get img_path list from api
    # TODO download img from list using for loop
