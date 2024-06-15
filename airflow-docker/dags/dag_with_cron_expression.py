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
    dag_id='dag_with_cron_expression_v3',
    description='This is an example of dags with cron expression',
    start_date=datetime(year=2024, month=5, day=1),
    schedule_interval='0 3 * * Tue',
    catchup=True
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command="echo This is an example of dags with cron expression"
    )

    task1