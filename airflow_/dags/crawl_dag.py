import os
from datetime import datetime, timedelta

import pendulum

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.sensors.gcs import GCSObjectExistenceSensor
from airflow.providers.google.cloud.transfers.gcs_to_sftp import GCSToSFTPOperator
from airflow.providers.google.cloud.transfers.local_to_gcs import (
    LocalFilesystemToGCSOperator,
)
from airflow.providers.google.cloud.transfers.postgres_to_gcs import (
    PostgresToGCSOperator,
)
from airflow.providers.google.cloud.transfers.sftp_to_gcs import SFTPToGCSOperator
from airflow.providers.sftp.sensors.sftp import SFTPSensor
from airflow.providers.slack.hooks.slack_webhook import SlackWebhookHook
from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow.utils.dates import days_ago
from callback.slack_noti import (
    send_slack_dag_success,
    send_slack_task_failure,
    send_slack_task_retry,
)
from database.metadata2db import df2db
from pytz import timezone

# package for tasks

local_tz = pendulum.timezone("Asia/Seoul")
scraped_time = datetime.now(timezone("Asia/Seoul")).strftime("%m-%d_%H")
# scraped_time="01-31_16"


AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME")
ssh_base = "/opt/ml/final-project-level3-cv-06"
keyword = "animal"
site = "pixabay"
n_imgs = 100
bucket = "scraped-img"
instance_name = "airflow-server"
zone_name = "us-west1-b"

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
    "on_failure_callback": send_slack_task_failure,
    # "on_success_callback": send_slack_dag_success,
    "on_retry_callback": send_slack_task_retry,
    # 'trigger_rule': 'all_success'
    "description": "A job for crawling img in pixabay",
    "tags": ["img", "crawler"],
}
##################     DAGS     ##################
with DAG("crawling", default_args=default_args, schedule="@once") as dag:

    #####################    JOBS    #######################
    crawl_img = BashOperator(
        task_id="img_crawler",
        bash_command=f"python {AIRFLOW_HOME}/dags/pixabay/scrape_api.py {keyword} {site} {scraped_time} {n_imgs}",
    )

    metadata2db = PythonOperator(
        task_id="metadata2db",
        python_callable=df2db,
        op_kwargs={"keyword": keyword, "site": site, "scraped_time": scraped_time},
    )
    img2gcs = LocalFilesystemToGCSOperator(
        task_id="img2gcs",
        src=f"{AIRFLOW_HOME}/dags/data/{keyword}/{site}/{scraped_time}/*.webp",
        dst=f"{keyword}/{site}/{scraped_time}/",
        bucket=bucket,
        gcp_conn_id="gcs_connection",
    )
    metadata2gcs = LocalFilesystemToGCSOperator(
        task_id="metadata2gcs",
        src=f"{AIRFLOW_HOME}/dags/data/{keyword}/{site}/{scraped_time}/metadata.feather",
        dst=f"{keyword}/{site}/{scraped_time}/",
        bucket=bucket,
        gcp_conn_id="gcs_connection",
    )
    # load_img_from_gcs2ssh = SSHOperator(
    #     task_id="download_img_from_gcs2ssh",
    #     ssh_conn_id="ssh_connection",
    #     command=f"python {ssh_base}/airflow_/dags/classification/load_img_from_gcs.py {scraped_time} {bucket} {site} {keyword}",
    # )
    load_img_from_gcs2ssh = GCSToSFTPOperator(
        task_id="download_img_from_gcs2ssh",
        source_bucket=bucket,
        source_object=f"{keyword}/{site}/{scraped_time}/[0-9]*.webp",
        destination_path=f"{ssh_base}/airflow_/dags/classification/data/{keyword}/{site}/",
        gcp_conn_id="gcs_connection",
        sftp_conn_id="sftp_connection",
    )
    sense_ssh_file = SFTPSensor(
        task_id="sense_ssh_file",
        sftp_conn_id="sftp_connection",
        path=f"{ssh_base}/airflow_/dags/classification/data/{keyword}/{site}/{scraped_time}/metadata.feather",
    )

    sense_gcs_file = GCSObjectExistenceSensor(
        task_id="check_metadata_in_gcs",
        google_cloud_conn_id="gcs_connection",
        bucket=bucket,
        object=f"{keyword}/{site}/{scraped_time}/metadata.feather",
    )

    infer_label = SSHOperator(
        task_id="infer_label",
        ssh_conn_id="ssh_connection",
        command=f"source /opt/ml/.local/share/virtualenvs/airflow_-dXXA5isc/bin/activate \
            && python {ssh_base}/airflow_/dags/classification/infer_animal.py {keyword} {site} {scraped_time}",
        cmd_timeout=600,
    )
    df2api = SSHOperator(
        task_id="df2api_remove_dir",
        ssh_conn_id="ssh_connection",
        command=f"source /opt/ml/.local/share/virtualenvs/airflow_-dXXA5isc/bin/activate \
            && python {ssh_base}/airflow_/dags/classification/df2api.py {keyword} {site} {scraped_time}",
    )
    img2ani = SSHOperator(
        task_id="img2ani",
        ssh_conn_id="ssh_connection",
        command=f"source /opt/ml/.local/share/virtualenvs/airflow_-dXXA5isc/bin/activate \
            && python {ssh_base}/airflow_/dags/paint_transformer/img2ani.py {keyword} {site} {scraped_time}",
        cmd_timeout=600,
    )
    ani2gcs = SFTPToGCSOperator(
        task_id="ani2gcs",
        source_path=f"{ssh_base}/airflow_/dags/classification/data/{keyword}/{site}/{scraped_time}/*_ani.webp",
        destination_bucket=bucket,
        destination_path=f"{keyword}/{site}/{scraped_time}",
        gcp_conn_id="gcs_connection",
        sftp_conn_id="sftp_connection",
    )
    # remove_dir = SSHOperator(
    #     task_id="remove_dir",
    #     ssh_conn_id="ssh_connection",
    #     command=f"rm -rf {ssh_base}/airflow_/dags/classification/data/{keyword}/{site}/{scraped_time}",
    # )
    slack_success_noti = SlackWebhookHook(
        task_id="slack_success_noti",
        http_conn_id="slack_connection",
        message=""":large_green_circle: Airflow Dag Succeeded.""",
    )
    #####################    TASKS    #####################
    (
        crawl_img
        >> [metadata2db, img2gcs]
        >> metadata2gcs
        >> sense_gcs_file
        >> load_img_from_gcs2ssh
        >> sense_ssh_file
        >> infer_label
        >> df2api
        >> img2ani
        >> ani2gcs
        # >> remove_dir
        >> slack_success_noti
    )

# TODO handling errors
# TODO configure the retries % failures
# TODO 새로 올라온 데이터에 대해서만 크롤링 후 db에 저장하도록 수정
# TODO gcs에 저장된 데이터와 local 데이터 중복 없도록 업로드
