import json
from datetime import timedelta, datetime

from airflow import DAG
from airflow.contrib.sensors import file_sensor
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.contrib.operators.file_to_gcs import FileToGoogleCloudStorageOperator
import convert_json_to_csv



seven_days_ago = datetime.combine(datetime.today() - timedelta(1),
                                  datetime.min.time())

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': seven_days_ago,
    'email': ['raghu.porumamilla@springml.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('site-visits-dag', default_args=default_args, schedule_interval='@daily')

#t1 = file_sensor(
#    task_id='local_file',
#    fs_conn_id='fs_default',
#    file_path='/Users/raghu/git-hub/demo/incoming/site-visits.json',
#    dag=dag)
t1 = DummyOperator(task_id='op1', dag=dag)
t2 = PythonOperator(
    task_id='python_task',
    python_callable=convert_json_to_csv.main,
    dag=dag
)
t3 = FileToGoogleCloudStorageOperator(
    task_id='fileToGCS',
    src='/usr/local/demo/outgoing/site-visits.csv',
    dst='site-visits',
    bucket='springml-demo',
    google_cloud_storage_conn_id='google_cloud_default',
    dag=dag
)

t3.set_upstream(t2)
t2.set_upstream(t1)
