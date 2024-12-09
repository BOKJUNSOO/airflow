from airflow import DAG
import pendulum
import datetime
import random
from airflow.operators.python import PythonOperator

with DAG(
    dag_id = "dags_python_operator",
    schedule = "10 0 * * 6#1", # 10분 0시 매월 매일 첫번째주 토요일
    start_date= pendulum.datetime(2024 , 12, 1, tz = "Asia/Seoul"),
    catchup=False
) as dag:
    def select_fruit():
        fruit = ["APPLE","BANANA","ORANGE","AVOCADO"]
        rand_int = random.randint(0,3)
        print(fruit[rand_int])

    python_operator = PythonOperator(
        task_id = "python_operator",
        # 어떤 함수를 실행할 것인지
        python_callable = select_fruit
    )

    # task
    python_operator