from airflow import DAG
import pendulum
import datetime
from airflow.operators.bash import BashOperator

with DAG(
    dag_id = "dags_bash_select_fruit",
    schedule = "10 0 * * 6#1", # 10분 0시 매월 매일 첫번째주 토요일
    start_date= pendulum.datetime(2024 , 12, 1, tz = "Asia/Seoul"),
    catchup=False
) as dag:
    
    t1_apple = BashOperator(
        task_id = "t1_apple",
        bash_command="/opt/airflow/plugins/shell/select_fruit.sh APPLE" # wsl의 airflow와 컨테이너 plugins 맵핑되어 있기 때문에 가능
    )

    t2_orange = BashOperator(
        task_id = "t2_orange",
        bash_command = "/opt/airflow/plugins/shell/select_fruit.sh ORANGE"
    )

    t1_apple >> t2_orange