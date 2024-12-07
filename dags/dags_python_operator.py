from airflow import DAG
import pendulum
import datetime
from airflow.operators.python import PythonOperator

with DAG(
    dag_id = "dags_python_operator",
    schedule = "10 0 * * 6#1", # 10분 0시 매월 매일 첫번째주 토요일
    start_date= pendulum.datetime(2024 , 12, 1, tz = "Asia/Seoul"),
    catchup=False
) as dag:
    python_operator = PythonOperator(
        task_id = "python_operator",
    )
