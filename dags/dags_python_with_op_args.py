from airflow import DAG
import pendulum
import datetime
import random
from airflow.operators.python import PythonOperator
from common.common_func import regis

with DAG(
    dag_id = "dags_python_with_op_args",
    start_date = pendulum.datetime(2024, 12, 1 , tz = "Asiz/Seoul"),
    schedule= "30 6 * * *",
    catchup= False,
) as dag:

    regist_t1 = PythonOperator(
        task_id = "regist_t1",
        python_callable= regis,
        # 함수에 전달할 인자를 리스트 형태로 지정한다
        op_args = ["bokjunsoo","man","kr","seoul"]


    )

    regist_t1