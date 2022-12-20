from datetime import datetime, timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'Loc Nguyen',
    'start_date': days_ago(0),
    'email': ['lc.nguyendang123@gmail.com'],
    'email_on_failure': False,
    'email_on-retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=2),
}

def greet(ti):
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    age = ti.xcom_pull(task_ids='get_age', key='age')
    print(f"Hello, My name is {first_name} {last_name}! I'm {age} years old")
    
def get_name(ti):
    ti.xcom_push(key='first_name', value='Loc')
    ti.xcom_push(key='last_name', value='Nguyen')

def get_age(ti):
    ti.xcom_push(key='age', value=20)
    
with DAG(
    dag_id='dag_with_python_operator',
    default_args=default_args,
    description='Dag with python operator',
    start_date=datetime(2022, 12, 16, 2),
    schedule_interval='@daily'
) as dag:
    
    task1 = PythonOperator(
        task_id='get_name',
        python_callable=get_name,
    )

    task2 = PythonOperator(
        task_id='get_age',
        python_callable=get_age,
    )

    task3 = PythonOperator(
        task_id='greet',
        python_callable=greet,
    )
    
    [task1, task2] >> task3
