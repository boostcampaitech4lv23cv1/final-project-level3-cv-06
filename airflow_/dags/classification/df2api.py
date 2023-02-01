import os
import sys

import requests

AIRFLOW_HOME = os.path.dirname(os.path.abspath(__file__))
KEYWORD, SITE, SCRAPED_TIME = sys.argv[1:]


def metadata2fastapi():
    base_path = f"{AIRFLOW_HOME}/data"
    file_path = os.path.join(
        base_path, KEYWORD, SITE, SCRAPED_TIME, "metadata_with_label.feather"
    )

    url = "http://34.64.169.197:/api/v1/meta/create"
    with open(file_path, "rb") as f:
        feather = f.read()
    file = {"file": feather}
    category = {"category": KEYWORD}
    try:
        res = requests.post(url, files=file, data=category)
        res.raise_for_status()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    metadata2fastapi()
