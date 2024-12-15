from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.decorators import task
from datetime import datetime
import pendulum

with DAG(
    dag_id = "dags_python_template",
    schedule="30 9 * * *",
    start_date=pendulum.datetime(2024,12,1, tz = "Asia/Seoul"),
    catchup=False
) as dag:
    
    def python_fuction1(start_date, end_date, **kwargs):
        print(start_date)
        print(end_date)
    
    python_t1 = PythonOperator(
        task_id = "python_t1",
        python_callable=python_fuction1,
        # python_function1에 인자로 입력하는 값을 딕셔너리로 정의
        # op_kwargs는 template 변수이므로 저장된 변수를 꺼내쓸수 있다.
        op_kwargs={
            'start_date' : '{{data_interval_start | ds}}',
            'end_date' : '{{data_interval_end | ds}}'
        }
    )

    @task(task_id='python_t2')
    def python_function2(**kwargs):
        # kwargs 에는 사용가능한 jinja template값이 모두 저장되어 있다.
        print(kwargs)
        print('ds:', kwargs['ds'])
        print('ts:', kwargs['ts'])
        print('date_interval_start:', str(kwargs['data_interval_start']))
        print('data_interval_end:', str(kwargs['data_interval_end']))
        print('task_instance:', str(kwargs['ti']))
    
    python_t1 >> python_function2()