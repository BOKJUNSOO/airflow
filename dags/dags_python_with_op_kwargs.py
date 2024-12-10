from airflow import DAG
import pendulum
import datetime
import random
from airflow.operators.python import PythonOperator
from common.common_func import regist2

with DAG (
    dag_id = "dags_python_with_op_kwargs",
    schedule="30 6 * * *",
    start_date= pendulum.datetime(2024, 12, 1, tz = "Asia/Seoul"),
    catchup= False
) as dag:
    
    regist2_t1 = PythonOperator(
        task_id = "regist2_t1",
        python_callable= regist2,
        # 명시적으로 앞에 두 인자를 받고 나머지 args 는 튜플로 출력
        op_args=["bokjunsoo","man","korea","seoul"],
        # 키워드 어규먼츠 / 딕셔너리 형태로 인자를 준다.
        # 함수스택내의 변수와 같은 key 가 있는지 우선적으로 확인한다
        op_kwargs={"email" : "brianbok97@gmail.com",
                   "phone" : "010"}
    )

    regist2_t1
