# Airflow
## Websites
* <https://airflow.apache.org/docs/stable/>
* <https://github.com/jghoman/awesome-apache-airflow>
* <https://marclamberti.com/>

## Commands
* airflow list_dags
* airflow list_tasks <dag_name>


# Concepts
<https://airflow.apache.org/docs/stable/concepts.html>

* DAG
* DAG runs
* Task
* Task Instances
* Task Lifecycle
![image missing.](https://airflow.apache.org/docs/stable/_images/task_lifecycle_diagram.png)
* Operator
	* DummyOperator
	* BashOperator
	* PythonOperator
	* HiveOperator
* Sensor
	* FileSensor
* Workflow
* Backfill_n_Catchup
* SubDAGs
	* SubDagOperator
* Hooks
* Branching
* XCOMs
* SLAs
	* t1 = BashOperator(task_id='t1', bash_command='sleep 15', sla=timedelta(seconds=5), retries=0)
* Plugins ($AIRFLOW_HOME/plugins)

