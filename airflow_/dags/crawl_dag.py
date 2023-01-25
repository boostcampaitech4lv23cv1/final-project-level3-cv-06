import os
from datetime import datetime, timedelta

import pendulum

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.sensors.gcs import GCSObjectExistenceSensor
from airflow.providers.google.cloud.transfers.gcs_to_local import (
    GCSToLocalFilesystemOperator,
)
from airflow.providers.google.cloud.transfers.local_to_gcs import (
    LocalFilesystemToGCSOperator,
)
from airflow.providers.google.cloud.transfers.postgres_to_gcs import (
    PostgresToGCSOperator,
)
from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow.utils.dates import days_ago
from database.metadata2db import df2db
from pytz import timezone

# package for tasks

local_tz = pendulum.timezone("Asia/Seoul")
now_time = datetime.now(timezone("Asia/Seoul")).strftime("%m-%d_%H:%M:%S")

AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME")

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
    # from pixabay.scrape_img import crawl_img_by_category

    # img_job = PythonOperator(
    #     task_id="img_crawler", python_callable=crawl_img_by_category
    # )
    crawl_img = BashOperator(
        task_id="img_crawler",
        bash_command="python ${AIRFLOW_HOME}/dags/pixabay/scrape_api.py",
    )

    metadata2db = PythonOperator(
        task_id="metadata2db",
        python_callable=df2db,
        op_kwargs={"keyword": "animals"},
    )
    img2gcs = LocalFilesystemToGCSOperator(
        task_id="img2gcs",
        src=f"{AIRFLOW_HOME}/dags/pixabay/crawled_img/animals/*.jpg",
        dst=f"{now_time}/",
        bucket="pixabay_animals",
        gcp_conn_id="my_gcs_connection",
    )
    metadata2gcs = LocalFilesystemToGCSOperator(
        task_id="metadata2gcs",
        src=f"{AIRFLOW_HOME}/dags/pixabay/crawled_img/animals/*.feather",
        dst=f"{now_time}/",
        bucket="pixabay_animals",
        gcp_conn_id="my_gcs_connection",
    )
    load_img_from_gcs = GCSToLocalFilesystemOperator(
        task_id="load_img_from_gcs",
        bucket="pixabay_animals",
        object_name=f"{now_time}/*.jpg",
        filename=f"{AIRFLOW_HOME}/dags/pixabay/crawled_img/animals/",
        gcp_conn_id="my_gcs_connection",
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
    crawl_img >> [metadata2db, img2gcs] >> metadata2gcs

# TODO handling errors
# TODO configure the retries % failures
# TODO Use Airflow's Sensors to detect external events or conditions before executing tasks
# TODO 새로 올라온 데이터에 대해서만 크롤링 후 db에 저장하도록 수정
# TODO gcs에 저장된 데이터와 local 데이터 중복 없도록 업로드
# TODO gcs에 업로드 시 메타 데이터까지 업로드
