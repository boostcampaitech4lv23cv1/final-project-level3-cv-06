import os
from datetime import datetime, timedelta

import pendulum

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.sensors.gcs import GCSObjectExistenceSensor
from airflow.providers.google.cloud.transfers.local_to_gcs import (
    LocalFilesystemToGCSOperator,
)
from airflow.providers.google.cloud.transfers.postgres_to_gcs import (
    PostgresToGCSOperator,
)
from airflow.providers.sftp.sensors.sftp import SFTPSensor
from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow.utils.dates import days_ago
from database.metadata2db import df2db
from pytz import timezone

# package for tasks

local_tz = pendulum.timezone("Asia/Seoul")
scraped_time = datetime.now(timezone("Asia/Seoul")).strftime("%m-%d_%H")

AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME")
ssh_base = "/opt/ml/final-project-level3-cv-06"
keyword = "animals"
site = "pixabay"
bucket = "scraped-img"
# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    "owner": "airflow",
    # "depends_on_past": False,
    "start_date": datetime(2023, 1, 12, 9, 0, 0, tzinfo=local_tz),
    "retries": 3,
    # "retry_delay": timedelta(minutes=1),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': task_fail_slack_alert,
    # 'on_success_callback': task_success_slack_alert,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
    "description": "A job for crawling img in pixabay",
    "tags": ["img", "crawler"],
}
##################     DAGS     ##################
with DAG("crawling", default_args=default_args, schedule="@once") as dag:

    #####################    JOBS    #######################
    crawl_img = BashOperator(
        task_id="img_crawler",
        bash_command=f"python {AIRFLOW_HOME}/dags/pixabay/scrape_api.py {scraped_time} {site}",
    )

    metadata2db = PythonOperator(
        task_id="metadata2db",
        python_callable=df2db,
        op_kwargs={"keyword": keyword, "site": site, "scraped_time": scraped_time},
    )
    img2gcs = LocalFilesystemToGCSOperator(
        task_id="img2gcs",
        src=f"{AIRFLOW_HOME}/dags/data/{keyword}/{site}/{scraped_time}/*.jpg",
        dst=f"{keyword}/{site}/{scraped_time}/",
        bucket=bucket,
        gcp_conn_id="my_gcs_connection",
    )
    # TODO jpg 2 webp
    metadata2gcs = LocalFilesystemToGCSOperator(
        task_id="metadata2gcs",
        src=f"{AIRFLOW_HOME}/dags/data/{keyword}/{site}/{scraped_time}/metadata.feather",
        dst=f"{keyword}/{site}/{scraped_time}/",
        bucket=bucket,
        gcp_conn_id="my_gcs_connection",
    )
    load_img_from_gcs2ssh = SSHOperator(
        task_id="download_img_from_gcs2ssh",
        ssh_conn_id="my_ssh_connection",
        command=f"python {ssh_base}/airflow_/dags/classification/load_img_from_gcs.py {scraped_time} {bucket} {site} {keyword}",
    )
    sense_ssh_file = SFTPSensor(
        task_id="sense_ssh_file",
        sftp_conn_id="my_sftp_connection",
        path=f"{ssh_base}/airflow_/dags/classification/data/{keyword}/{site}/{scraped_time}/metadata.feather",
    )

    # check_gcs_file = GCSObjectExistenceSensor(
    #     task_id="check_gcs_file",
    #     google_cloud_conn_id="my_gcs_connection",
    #     bucket="pixabay_animals",
    #     object="animals.csv",
    # )

    # infer_job = BashOperator(
    #     task_id="infer_animal",
    #     bash_command=f"python ${AIRFLOW_HOME}/dags/classification/infer_animal.py",
    # )

    # from classification.infer_animal import infer_senddb

    # infer_job = PythonOperator(task_id="infer_animal", python_callable=infer_senddb)

    #####################    TASKS    #####################
    (
        crawl_img
        >> [metadata2db, img2gcs]
        >> metadata2gcs
        >> load_img_from_gcs2ssh
        >> sense_ssh_file
    )

# TODO handling errors
# TODO configure the retries % failures
# TODO Use Airflow's Sensors to detect external events or conditions before executing tasks
# TODO 새로 올라온 데이터에 대해서만 크롤링 후 db에 저장하도록 수정
# TODO gcs에 저장된 데이터와 local 데이터 중복 없도록 업로드
# TODO 버킷 안에 있는 폴더명 어떻게 할지 정하기 (datetime을 쓰면 task 실패 시 datetime을 다시 실행하기 때문에 폴더가 여러개 생기는 문제 발생)
# TODO slack 알림 설정