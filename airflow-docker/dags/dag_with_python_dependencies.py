from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'sjahchan',
    'retry': 5,
    'retry_delay': timedelta(minutes=5)
}


def get_sklearn():
    import sklearn
    print(f'Scikit-learning installed wit version: {sklearn.__version__}')

def get_matplotlib():
    import matplotlib
    print(f'Math Plot Lib version: {matplotlib.__version__}')

with DAG(
    default_args=default_args,
    dag_id='dag_with_python_dependencies_v02',
    description='Dag to test the correct creation of a airflow extending image with \
          the scikit-learn library',
    start_date=datetime(year=2024, month=6, day=14),
    schedule_interval='@daily'
) as dag:
    get_sklearn = PythonOperator(
        task_id='get_sklearn_version',
        python_callable=get_sklearn
    )
    get_matplotlib = PythonOperator(
        task_id='get_matplotlib_version',
        python_callable=get_matplotlib
    )

    get_sklearn  >> get_matplotlib
