from airflow import DAG
from airflow.decorators import task
import pendulum
with DAG(
    dag_id = "dags_python_with_macro",
    schedule="0 0 * * *",
    start_date = pendulum.datetime(2024,12,1 , tz = "Asia/Seoul"),
    catchup=False

) as dag:
    # airflow template 를 사용
    @task(
        task_id = "get_datetime_macro",
        templates_dict={
            'start_date' : '{{(data_interval_start.in_timezone("Asia/Seoul") + macros.datetime.relativedelta.relativedelta(months = -1, day= 1))|ds}}',
            'end_date' : '{{(data_interval_end.in_timezone("Asia/Seoul").replace(day=1) + macros.datetime.relativetimedelta.relativetimedelta(days=-1))|ds}}'
        }
    )
    def get_date_time_macro(**kwargs):
        # task에서 정의됐던 templates_dict 자체가 kwargs의 키로 저장된다.
        # 해당 키는 벨류를 가지고 있다.
        templates_dict = kwargs.get('templates_dict') or {}
        if templates_dict:
            start_date = templates_dict.get('start_date') or 'start_date'
            end_date = templates_dict.get('end_date')
            print(start_date)
            print(end_date)
    
    # airflow template 를 사용하지 않고 python 문법 사용
    @task(task_id="task_direct_calc")
    def get_direct_calc(**kwargs):
        from dateutil.relativedelta import relativedelta
        data_interval_end = kwargs['data_interval_end']

        # 직접연산
        # 전월 1일
        prev_month_date_first = data_interval_end.in_timezone('Asia/Seoul') + relativedelta(months=-1, day = 1)
        # 전월 말일
        prev_month_day_last = data_interval_end.in_timezone('Asia/Seoul').replace(day=1) + relativedelta(days=-1)
        print(prev_month_date_first.strftime("%Y-%m-%d"))
        print(prev_month_day_last.strftime("%Y-%m-%d"))

    get_date_time_macro() >> get_direct_calc()