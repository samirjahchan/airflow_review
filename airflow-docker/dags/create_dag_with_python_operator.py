from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'sjahchan',
    'retries': 5,
    'retry_daley': timedelta(minutes=5)
}

def greet(ti):
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    age = ti.xcom_pull(task_ids='get_age', key='age')
    print(f'Hello world! my name is: {first_name} {last_name} \
          and I am {age} years old.')

def get_name(ti):
    first_name = ti.xcom_push(key='first_name', value='Jerry')
    last_name = ti.xcom_push(key='last_name', value='Rodrigues')


def get_age(ti):
    age = ti.xcom_push(key='age', value=54)


with DAG(
    dag_id='our_first_python_operator_v7',
    default_args=default_args,
    description="This is forth python operator dag v7",
    start_date=datetime(year=2021, month=7, day=2),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        op_kwargs={
            "age": 54
        }
    )

    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )

    task3 = PythonOperator(
        task_id='get_age',
        python_callable=get_age
    )

    task2 >> task1
    task3 >> task1