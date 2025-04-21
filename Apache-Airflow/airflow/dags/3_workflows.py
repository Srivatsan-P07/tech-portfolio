import random
from datetime import datetime

# AirFlow
from airflow import DAG

# Utils
from airflow.utils.task_group import TaskGroup

# Operators
from airflow.operators.python import BranchPythonOperator
from airflow.operators.dummy import DummyOperator

def brancher():
    value = random.randint(1,10)
    print(value, value%2)
    if value%2 == 0:
        return 'Task-Group'
    else:
        return 'branch2'

def brancher2():
    value = random.randint(1,10)
    print(value, value%2)
    if value%2 == 0:
        return 'Task-Group.tg-branch1'
    else:
        return 'Task-Group.tg-branch2'

with DAG('3_workflows', start_date = datetime(2025, 4, 21), schedule_interval = '@daily', catchup = False) as dag:

    task1 = BranchPythonOperator(
        task_id = 'Branch-Python-Operator',
        python_callable = brancher
    )

    task2 = DummyOperator(task_id='branch2')
    
    with TaskGroup('Task-Group') as tg:
        task3 = BranchPythonOperator(
            task_id = 'Branch-Python-Operator-in-TG',
            python_callable = brancher2
        )

        task4 = DummyOperator(task_id = 'tg-branch1')
        task5 = DummyOperator(task_id = 'tg-branch2')

        task3 >> task4
        task3 >> task5

    task1 >> task2
    task1 >> task3