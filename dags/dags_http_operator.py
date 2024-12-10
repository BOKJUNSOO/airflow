from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow import DAG
import pendulum
import datetime
import random
from airflow.decorators import task
with DAG(
    dag_id = "dags_http_operator",
    start_date = pendulum.datetime(2024, 12, 1, tz = "Asia/Seoul"),
    schedule= "0 0 * * *",
    catchup=False
) as dag:
    s_dot_env = SimpleHttpOperator(
        task_id = "s_dot_env",
        http_conn_id = "openapi.seoul",
        # 전역변수 variable
        endpoint = "{{var.value.apikey_openapi_seoul_go_kr}}/json/airPolutionMeasuringPlace/1/5",
        method = "GET",
        headers = {
            'Content-Type':'application/json',
            'charset':'utf-8',
            'Accept': '*/*'
        }
    )

    @task(task_id = "python_2")
    def python_2(**kwargs):
        ti = kwargs["ti"]
        rslt = ti.xcom_pull(task_id = "s_dot_env")
        import json
        from pprint import pprint
        pprint(json.loads(rslt))

    s_dot_env >> python_2()