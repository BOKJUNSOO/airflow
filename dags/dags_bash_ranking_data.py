from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
    dag_id = "dags_bash_ranking_data",
    start_date= pendulum.datetime(2024, 12, 10, tz = "Asia/Seoul"),
    schedule= "0 0 * * *",
    catchup = False
) as dag:
    
    start_sign = BashOperator(
        task_id = "start_sign",
        bash_command="echo start download"
    )

    download_task = BashOperator(
        task_id = "download_task",
        bash_command="/opt/airflow/plugins/shell/download_data.sh {{var.value.apikey_openapi_nexon}}"
    )

    start_sign >> download_task