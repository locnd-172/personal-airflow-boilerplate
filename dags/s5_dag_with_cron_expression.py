from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta 

dag_owner = 'Loc Nguyen'

default_args = {
    'owner': dag_owner,
    'depends_on_past': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='dag_with_cron_expression',
    default_args=default_args,
    start_date=datetime(2022, 12, 5),
    # schedule_interval='@daily',
    schedule_interval='0 0 * * *', # minute hour day_of_month month day_of_week (crontab.guru)
    tags=['cron_exp']
):

    task1 = BashOperator(
        task_id='task1',
        bash_command='echo dag with cron exp!'
    )

    task1 