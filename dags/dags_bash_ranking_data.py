from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator
from airflow.providers.http.operators.http import SimpleHttpOperator

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

    ranking_data = SimpleHttpOperator(
        task_id = "ranking_data",
        http_conn_id = "openapi.nexon",
        endpoint = "https://open.api.nexon.com/maplestory/v1/ranking/overall?date=2024-12-10&world_name=%EC%97%98%EB%A6%AC%EC%8B%9C%EC%9B%80&page=1",
        method = "GET",
        headers = {
            'x-nxopen-api-key':'{{var.value.apikey_openapi_nexon}}'
        }
    )

    start_sign >> ranking_data
