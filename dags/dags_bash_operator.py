from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator
# DAG 파일을 작성할때 우선적으로 작성
with DAG(
    # airflow ui 에 보이는 이름
    dag_id="dags_bash_operator", # dag 파일명과 일치시키는 것이 좋음

    # 
    schedule="0 0 * * *", # 매일 0시 0분에 실행

    # dag이 언제 돌 것인가
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"),

    # 1/1 부터 현재 시간까지 누락된 데이터를 모두 수집
    catchup=False,   # False로 해놓는것이 좋다.

    # dagrun_timeout=datetime.timedelta(minutes=60), # 60분 이상 돌면 실패

    # option - ui 상 파란색 박스
    tags=["example", "example2"],

    # task에 공통적으로 넘겨줄 parameter
    # params={"example_key": "example_value"},
) as dag:
    
    # 오퍼레이터를 통해 만들어지는 것이 task다
    bash_t1 = BashOperator(
        # ui graph
        # 객체명과 task 명을 같게 하자
        task_id="bash_t1",
        bash_command="echo whoami",
    )

    bash_t2 = BashOperator(
        task_id = "bash_t2",
        bash_command="echo $HOSTNAME"
    )

    bash_t1 >> bash_t2