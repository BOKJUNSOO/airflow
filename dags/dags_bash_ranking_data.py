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
    
    download_task = BashOperator(
        task_id = "download_task",
        bash_command=f"opt/airflow/plugins/shell/download.sh {{var.value.apikey_openapi_nexon}}"
    )