from airflow.providers.slack.hooks.slack_webhook import SlackWebhookHook


def send_slack_task_failure(context):
    slack_msg = f"""
    :red_circle: Airflow Task Failed.
    *Task*: {context.get('task_instance').task_id}
    *Dag*: {context.get('task_instance').dag_id}
    *Execution Time*: {context.get('execution_date')}
    *Log Url*: {context.get('task_instance').log_url}
    """

    slack_hook = SlackWebhookHook(slack_webhook_conn_id="slack_connection")
    slack_hook.send(text=slack_msg)


def send_slack_dag_success(context):
    slack_msg = f"""
    :large_green_circle: Airflow Dag Succeeded.
    *Dag*: {context.get('task_instance').dag_id}
    *Execution Time*: {context.get('execution_date')}
    *Log Url*: {context.get('task_instance').log_url}
    """

    slack_hook = SlackWebhookHook(slack_webhook_conn_id="slack_connection")
    slack_hook.send(text=slack_msg)


def send_slack_task_retry(context):
    slack_msg = f"""
    :large_yellow_circle: Airflow Task Retrying.
    *Task*: {context.get('task_instance').task_id}
    *Dag*: {context.get('task_instance').dag_id}
    *Execution Time*: {context.get('execution_date')}
    *Log Url*: {context.get('task_instance').log_url}
    """

    slack_hook = SlackWebhookHook(slack_webhook_conn_id="slack_connection")
    slack_hook.send(text=slack_msg)
