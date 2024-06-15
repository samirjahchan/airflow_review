from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'sjahchan',
    'retries': 5,
    'retry_daley': timedelta(minutes=2)
}

with DAG(
    dag_id='our_first_dag_v4',
    description="This is our first dag",
    start_date=datetime(year=2021, month=7, day=2),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo Hello World!!!"
    )

    task2 = BashOperator(
        task_id='second_task',
        bash_command="echo Second Task!!"
    )

    task3 = BashOperator(
        task_id='third_task',
        bash_command="echo hey, I am the task3 and will be running after task1"
    )

    task1 >> task2
    task1 >> task3