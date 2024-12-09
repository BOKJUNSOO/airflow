from airflow import DAG
import pendulum
import datetime
from airflow.operators.python import PythonOperator
from airflow.decorators import task

with DAG(
    dag_id = "dags_python_taskdeco",
    schedule = "10 0 * * 6#1", 
    start_date= pendulum.datetime(2024 , 12, 1, tz = "Asia/Seoul"),
    catchup=False
) as dag:
    
    @task(task_id = "python_task_1")
    def print_context(some_input):
        print(some_input)

    python_task = print_context("task_decorator_실행")