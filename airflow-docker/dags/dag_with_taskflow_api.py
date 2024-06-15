from datetime import datetime, timedelta

from airflow.decorators import dag, task

default_args = {
    'owner': 'sjahchan',
    'retries': 2,
    'retry_delay': timedelta(minutes=5)
}

@dag(
        default_args=default_args,
        dag_id='dag_with_taskflow_api_v3', 
        description='This is a DAG with API',
        start_date=datetime(year=2024, month=6, day=14),
        schedule_interval='@daily'
)
def hello_world_etl():
    
    @task(multiple_outputs=True)
    def get_name():
        return { 
                'first_name': 'Samir Duenhas',
                'last_name':  'Jahchan'
        }
    
    @task()
    def get_age():
        return 54
    
    @task()
    def greet(first_name: str, last_name: str, age: int):
        print(f'Hello, my name is {first_name} {last_name}, and I am {age} years old!')

    name_dic = get_name()
    age = get_age()
    greet(
        first_name=name_dic['first_name'], 
        last_name=name_dic['last_name'], 
        age=age
    )

greet_dag = hello_world_etl()
