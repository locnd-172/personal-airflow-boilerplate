from datetime import datetime, timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'Loc Nguyen',
    'start_date': days_ago(0),
    'email': ['lc.nguyendang123@gmail.com'],
    'email_on_failure': False,
    'email_on-retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=2),
}

with DAG(
    dag_id='first_dag',
    default_args=default_args,
    description='My first dag',
    start_date=datetime(2022, 12, 17, 2),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo Hello, world!',
    )
    
    task2 = BashOperator(
        task_id='second_task',
        bash_command='echo I\'m second task!',
    )
    
    task3 = BashOperator(
        task_id='third_task',
        bash_command='echo I\'m third task!',
    )
    
    # Task dependency method 1
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)
    
    # Task dependency method 2
    # task1 >> task2
    # task1 >> task3 
    
    # Task dependency method 3
    task1 >> [task2, task3]
