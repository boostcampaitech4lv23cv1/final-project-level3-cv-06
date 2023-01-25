import os

AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME")


def download_img_from_gcs(datetime, bucket="pixabay_animals"):
    dest = f"{AIRFLOW_HOME}/dags/classification/data/{datetime}/img/"
    os.makedirs(dest, exist_ok=True)
    bash_script = f"gsutil -m cp -r gs://{bucket}/animals/{datetime}/ {dest}"
    os.system(bash_script)


if __name__ == "__main__":
    download_img_from_gcs(datetime="01-25_04:00:03", bucket="pixabay_animals")
