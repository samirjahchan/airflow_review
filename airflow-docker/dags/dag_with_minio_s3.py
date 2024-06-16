from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor

default_args = {
    'owner': 'sjahchan',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    default_args=default_args,
    dag_id='dag_with_minio_v1',
    description='This is a dag sensor operator against AWS S3 like MINio',
    start_date=datetime(year=2024, month=6, day=14),
    schedule_interval='@daily'
):
    task1=S3KeySensor(
        task_id='sensor_minio_s3',
        bucket_name='airflow',
        bucket_key='data.csv',
        aws_conn_id='minio_conn'
    )