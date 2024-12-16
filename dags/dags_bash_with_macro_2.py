from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
import pendulum

with DAG(
    dag_id = "dags_bash_with_macro_2",
    # 매월 둘째주 토요일
    schedule="10 0 * * 6#2",
    start_date=pendulum.datetime(2024,12,12 , tz = "Asia/Seoul"),
    catchup=False
) as dag:
    # START_DATA : 2주전 월요일, END_DATE: 2주전 토요일
    task_1 = BashOperator(
        task_id = "task_1",
        env={
            'START_DATE':'{{(date_interval_start.in_timezone("Asia/Seoul") + macros.datetime.timedelta(days=16))|ds}}',
            'END_DATE':'{{(date_interval_end.in_timezone("Asia/Seoul") - macros.datetime.timedelta(days=14))|ds}}'
        },
        bash_command='echo "START_DATE: $START_DATE" && echo "END_DATE: $END_DATE" '
        
    )