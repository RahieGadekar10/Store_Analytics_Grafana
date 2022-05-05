import airflow
from airflow.models import DAG 
from airflow.operators.bash_operator import BashOperator 
from airflow.oeprators.dummy_operator import DummyOperator
from datetime import datetime

with DAG(dag_id = "sql_sqoop" , schedule_interval = "@daily" , start_date = datetime(2020,1,1) , catchup = False) as sqoop_dag : 
	
	opt1 = DummyOperator(task_id = "Started")
	opt2 = BashOperator(task_id = "Storing_Data_In_HDFS" , bash_command = "sqoop --exec sqoopsql")
	opt3 = DummyOperator(task_id = "Finished")

opt1>>opt2>>opt3

