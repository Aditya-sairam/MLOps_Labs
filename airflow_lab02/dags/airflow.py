from airflow import DAG
# from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta 
import sys
import os 

from src.wine_data_processing import load_data_task, clean_data_task, train_model_task, evaluate_model_task

default_args = {
    'owner': 'airflow2',
    'depends_on_past': False,
    'start_date': datetime(2026, 2, 12),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'wine_ml_pipeline',
    default_args=default_args,
    description='A simple ML pipeline for wine quality prediction',
    schedule_interval= '@daily',
    catchup=False
)

load_data = PythonOperator(
    task_id="load_data",
    default_args=default_args,
    python_callable=load_data_task,
    dag=dag 
)

clean_data = PythonOperator(
    task_id="clean_data",
    python_callable=clean_data_task,
    dag=dag
)

train_model = PythonOperator(
    task_id='train_model',
    python_callable=train_model_task,
    dag=dag,
)

evaluate_model = PythonOperator(
    task_id='evaluate_model',
    python_callable=evaluate_model_task,
    dag=dag,
)

load_data >> clean_data >> train_model >> evaluate_model
