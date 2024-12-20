from airflow import DAG
import pendulum
from airflow.operators.python import BranchPythonOperator, PythonOperator

with DAG(
    dag_id = "dags_branch_python_operator",
    start_date=pendulum.datetime(2024,12,12, tz ="Asia/Seoul"),
    schedule="0 6 * * *",
    catchup=False
) as dag:
    def select_random():
        import random
        item_list=["A","B","C"]
        selected_item = random.choice(item_list)
        if selected_item == "A":
            return "task_a"
        elif selected_item in ["B","C"]:
            return ["task_b","task_c"]
    
    python_brach_task = BranchPythonOperator(
        task_id="python_branch_task",
        python_callable=select_random
    )

    def common_func(**kwargs):
        print(kwargs["selected"])

    task_a = PythonOperator(
        task_id = "task_a",
        python_callable=common_func,
        op_kwargs={"selected":"A"}
    )

    task_b = PythonOperator(
        task_id="task_b",
        python_callable=common_func,
        op_kwargs={"selected":"B"}
    )

    task_c = PythonOperator(
        task_id="task_c",
        python_callable=common_func,
        op_kwargs={"selected":"C"}
    )

    python_brach_task>>[task_a,task_b,task_c]