import os
import sys

AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME")


def download_img_from_gcs(scraped_time, bucket, site, keyword):
    dest = f"{AIRFLOW_HOME}/dags/classification/data/{keyword}/{site}/{scraped_time}"
    os.makedirs(dest, exist_ok=True)
    bash_script = (
        f"gsutil -m cp -r gs://{bucket}/{keyword}/{site}/{scraped_time}/ {dest}"
    )
    os.system(bash_script)


if __name__ == "__main__":
    scraped_time, bucket, site, keyword = sys.argv[1:]
    download_img_from_gcs(scraped_time, bucket, site, keyword)
# TODO args 설정 (datetime 넘겨주는 방식)
