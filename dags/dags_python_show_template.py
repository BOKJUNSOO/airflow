from airflow import DAG
import pendulum
import datetime
from airflow.decorators import task

with DAG(
    dag_id = "dags_python_show_template",
    schedule="30 0 * * *",
    start_date=pendulum.datetime(2024,12,1, tz = "Asia/Seoul"),
    catchup=True
) as dag:

    @task(task_id="python_task")
    def show_templates(**kwargs):
        from pprint import pprint
        # kwargs 에 parameter을 주지 않고, 담고있는 정보를 확인
        pprint(kwargs)
    
    show_templates()