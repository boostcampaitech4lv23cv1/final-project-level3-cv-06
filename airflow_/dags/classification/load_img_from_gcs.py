import os
import sys


def download_img_from_gcs(scraped_time, bucket, site, keyword):
    dest = f"/opt/ml/final-project-level3-cv-06/airflow_/dags/classification/data/{keyword}/{site}/"
    os.makedirs(dest, exist_ok=True)
    bash_script = (
        f"gsutil -m cp -r gs://{bucket}/{keyword}/{site}/{scraped_time}/ {dest}"
    )
    os.system(bash_script)


if __name__ == "__main__":
    scraped_time, bucket, site, keyword = sys.argv[1:]
    download_img_from_gcs(scraped_time, bucket, site, keyword)
