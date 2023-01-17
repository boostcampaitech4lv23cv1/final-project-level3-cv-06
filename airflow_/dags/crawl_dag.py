from datetime import datetime, timedelta

import pendulum

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

# package for tasks

local_tz = pendulum.timezone("Asia/Seoul")


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
    from pixabay.scrape_img import crawl_img_by_category

    img_job = PythonOperator(
        task_id="img_crawler", python_callable=crawl_img_by_category
    )

    from database.metadata2db import df2db

    send_data_job = PythonOperator(
        task_id="metadata2db",
        python_callable=df2db,
        op_kwargs={"keyword": "animal"},
    )
    infer_job = BashOperator(
        task_id="infer_animal",
        bash_command="python ${AIRFLOW_HOME}/dags/classification/infer_animal.py",
    )
    # from classification.infer_animal import infer_senddb
    # infer_job = PythonOperator(task_id="infer_animal", python_callable=infer_senddb)

    #####################    TASKS    #####################
    img_job >> send_data_job >> infer_job

# TODO handling errors
# TODO configure the retries % failures
# TODO notifications such as Slack or email
# TODO Use Airflow's Sensors to detect external events or conditions before executing tasks
# TODO 새로 올라온 데이터에 대해서만 크롤링 후 db에 저장하도록 수정
