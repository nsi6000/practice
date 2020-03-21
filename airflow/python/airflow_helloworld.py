from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

dag = DAG(
        dag_id='HelloWorld',
        start_date=datetime(2020,3,21),
        schedule_interval='* * * * *'
        )


t1 = BashOperator(
        task_id='task_1',
        bash_command='echo "Hello World from Task 1"',
        dag=dag
        )

t2 = BashOperator(
        task_id='task_2',
        bash_command='echo "Hello World from Task 2"',
        dag=dag
        )

t2.set_upstream(t1)

