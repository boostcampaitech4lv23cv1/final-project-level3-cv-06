import os
import shutil
import sys

import requests

AIRFLOW_HOME = os.path.dirname(os.path.abspath(__file__))
KEYWORD, SITE, SCRAPED_TIME = sys.argv[1:]
# KEYWORD, SITE, SCRAPED_TIME = "animal", "pixabay", "01-31_12"


def metadata2fastapi():
    base_path = f"{AIRFLOW_HOME}/data"
    file_path = os.path.join(
        base_path, KEYWORD, SITE, SCRAPED_TIME, "metadata_with_label.feather"
    )

    file = {"file": open(file_path, "rb")}
    url = "http://34.64.169.197:/api/v1/meta/create"
    res = requests.post(url, files=file)
    print(res.json())
    print(res.status_code)


def remove_dirs():
    base_path = f"{AIRFLOW_HOME}/data"
    path = os.path.join(base_path, KEYWORD, SITE, SCRAPED_TIME)
    shutil.rmtree(path)


if __name__ == "__main__":
    metadata2fastapi()
    remove_dirs()
