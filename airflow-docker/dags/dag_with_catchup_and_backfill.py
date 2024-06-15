from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'sjahchan',
    'retries': 2,
    'retry_delay': timedelta(minutes=5)
}
with DAG(
    default_args=default_args,
    dag_id='dag_with_cath',
    description='Simple dag with cath',
    start_date=datetime(year=2024, month=5, day=14),
    schedule_interval='@daily',
    catchup=False
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command="echo Simple dag with cath"
    )

    task1