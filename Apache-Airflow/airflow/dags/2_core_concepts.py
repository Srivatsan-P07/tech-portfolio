from datetime import datetime

# AirFlow
from airflow import DAG
from airflow.models import Variable

## Operators
from airflow.operators.dummy import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.email_operator import EmailOperator

## Providers
from airflow.providers.mysql.hooks.mysql import MySqlHook

# Start Program
Variable.set('my_key1', 'Srivatsan')

def func():
    hook = MySqlHook(mysql_conn_id='mysql_db_airflow')  # Use your Airflow Connection ID
    # Run a SQL statement (DDL or DML)
    hook.run("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100));")
    hook.run(" INSERT INTO users (name) VALUES ('Alice'); ")

    # Fetch records
    records = hook.get_records("SELECT * FROM users;")
    print(records)

def xcom_push_fn(**kwargs):
    ti = kwargs['ti']
    ti.xcom_push(key = 'my_key2', value = True)

def xcom_pull_fn(**kwargs):
    ti = kwargs['ti']
    output = ti.xcom_pull(task_ids = 'Xcom-Push', key = 'my_key2')
    return output

with DAG('2_core_concepts', start_date=datetime(2025, 4, 19), schedule_interval='@daily') as dag:
    task1 = DummyOperator(task_id='Dummy-Operator')
    
    task2 = BashOperator(
        task_id = 'Bash-Operator',
        bash_command = f" echo 'Bash Command Variable --> {Variable.get('my_key1')}' "
    )

    task3 = PythonOperator(
        task_id = 'Python-Operator',
        python_callable = func
    )

    task4 = PythonOperator(
        task_id = 'Xcom-Push',
        python_callable = xcom_push_fn,
        provide_context = True
    )

    task5 = PythonOperator(
        task_id = 'Xcom-Pull',
        python_callable = xcom_pull_fn,
        provide_context = True
    )

    # task4 = EmailOperator(
    #     task_id = 'Email-Operator',
    #     to = 'svs.vatsan7@gmail.com',
    #     subject = 'Hello from AirFlow',
    #     html_content = 'Hello from AirFlow'
    # )

    task1 >> task2 >> task3 >> task4 >> task5