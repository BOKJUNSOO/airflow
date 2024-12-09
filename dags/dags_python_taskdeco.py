from airflow import DAG
import pendulum
import datetime
from airflow.operators.python import PythonOperator
from airflow.decorators import task, dag

@dag(
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
)

@task(task_id = "python_task_1")
def print_context(some_input):
    print(some_input)

python_task = print_context("task_decorator_실행")