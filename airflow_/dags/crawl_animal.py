import os
import time
from datetime import datetime, timedelta

import pendulum

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.transfers.sftp_to_gcs import SFTPToGCSOperator
from airflow.providers.sftp.sensors.sftp import SFTPSensor
from airflow.providers.slack.operators.slack_webhook import SlackWebhookOperator
from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow.utils.dates import days_ago
from callback.slack_noti import send_slack_task_failure, send_slack_task_retry
from pytz import timezone

# package for tasks

local_tz = pendulum.timezone("Asia/Seoul")
scraped_time = datetime.now(timezone("Asia/Seoul")).strftime("%m-%d_%H")
# scraped_time="01-31_16"


AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME")
ssh_base = "/opt/ml/final-project-level3-cv-06"
keyword = "animal"
site = "pixabay"
n_imgs = 300
bucket = "scraped-img"
instance_name = "airflow-server"
zone_name = "us-west1-b"

# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization


default_args = {
    "owner": "airflow",
    # "depends_on_past": False,
    "start_date": datetime(2023, 2, 2, 9, 0, 0, tzinfo=local_tz),
    "retries": 3,
    # "retry_delay": timedelta(minutes=1),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    "on_failure_callback": send_slack_task_failure,
    "on_retry_callback": send_slack_task_retry,
    "description": "A job for crawling img in pixabay",
    "tags": ["img", "crawler"],
}
##################     DAGS     ##################
with DAG("crawling_animal", default_args=default_args, schedule="@daily") as dag:

    #####################    JOBS    #######################
    crawl_img = BashOperator(
        task_id="img_crawler",
        bash_command=f"python {AIRFLOW_HOME}/dags/pixabay/scrape_api.py {keyword} {site} {scraped_time} {n_imgs}",
    )

    load_data_from_gcs2ssh = SSHOperator(
        task_id="download_data_from_gcs2ssh",
        ssh_conn_id="ssh_connection",
        command=f"python {ssh_base}/airflow_/dags/classification/load_img_from_gcs.py {bucket}",
        conn_timeout=5 * n_imgs
    )
    infer_label = SSHOperator(
        task_id="infer_label",
        ssh_conn_id="ssh_connection",
        command=f"source /opt/ml/.local/share/virtualenvs/airflow_-dXXA5isc/bin/activate \
            && python {ssh_base}/airflow_/dags/classification/infer_animal.py {keyword} {site} {scraped_time}",
        cmd_timeout=30 * n_imgs,  # 30s * n_imgs
        conn_timeout=30 * n_imgs
    )
    sleep_for_ani = PythonOperator(
        task_id="sleep_for_ani",
        python_callable=lambda: time.sleep(n_imgs / 2),
    )
    ani2gcs = SFTPToGCSOperator(
        task_id="ani2gcs",
        source_path=f"{ssh_base}/airflow_/dags/classification/data/{keyword}/{site}/{scraped_time}/*_ani.webp",
        destination_bucket=bucket,
        destination_path=f"{keyword}/{site}/{scraped_time}",
        gcp_conn_id="gcs_connection",
        sftp_conn_id="sftp_connection",
    )
    remove_dir = SSHOperator(
        task_id="remove_dir",
        ssh_conn_id="ssh_connection",
        command=f"rm -rf {ssh_base}/airflow_/dags/classification/data/{keyword}/{site}/{scraped_time}",
    )
    slack_success_noti = SlackWebhookOperator(
        task_id="slack_success_noti",
        slack_webhook_conn_id="slack_connection",
        message=""":large_green_circle: Airflow Dag Succeeded.""",
    )
    #####################    TASKS    #####################
    (
        crawl_img
        >> load_data_from_gcs2ssh
        >> infer_label
        >> sleep_for_ani
        >> ani2gcs
        >> remove_dir
        >> slack_success_noti
    )

# TODO handling errors
# TODO configure the retries % failures
# TODO docker compose postgre 지우기
# TODO make sensor that sense gcp img files on ssh
