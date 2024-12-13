from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
import pendulum

with DAG(
    dag_id = "dags_bash_operator_with_template",
    start_date = pendulum.datetime(2024,12,1 , tz = "Asia/Seoul"),
    schedule="0 0 * * *",
    catchup=False

) as dag:
    bash_t1 = BashOperator(
        task_id = "bash_t1",
        # quoting  (bash 문법) 따라서 작성
        bash_command= 'echo "End date is {{ data_interval_end}}"'
    )

    bash_t2 = BashOperator(
        task_id = "bash_t2",
        # env parameter도 template 적용 가능, dictionary 형태로 전달
        env = {
                'START_DATE': '{{ data_interval_start | ds}}',
                'END_DATE' : '{{ data_interval_end | ds}}'
        },
        # 파이프로 ds 주면 yyyy-mm-dd 로 formating
        # 앞에커맨드가 성공하면 && 뒤에 커맨드 실행 (bash 문법)
        bash_command='echo "Start date is $START_DATE" &&'
                     'echo "End date is $END_DATE"'
    )

    bash_t1>>bash_t2