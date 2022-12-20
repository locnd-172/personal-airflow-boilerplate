from airflow.decorators import dag, task
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'Loc Nguyen',
    'start_date': days_ago(0),
    'email': ['lc.nguyendang123@gmail.com'],
    'email_on_failure': False,
    'email_on-retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=2),
}

@dag(
    dag_id='task_flow_api',
    default_args=default_args,
    start_date=datetime(2022, 12, 18),
    schedule_interval='@daily'
)
def hello_world_etl():
    
    @task(multiple_outputs=True)
    def get_name():
        return {
            'first_name': 'Loc',
            'last_name': 'Nguyen'
        }
    
    @task
    def get_age():
        return 20
    
    @task
    def greet(first_name, last_name, age):
        print(f"Hello! My name is {first_name} {last_name}, I'm {age} years old.")
        
    name_dict = get_name()
    age = get_age()
    greet(first_name=name_dict['first_name'], last_name=name_dict['last_name'], age=age)
    
    
greet_dag = hello_world_etl()