# Store Analytics
The data is generated from the store in the form of csv and trasnferred in real time to the MySql server. From the MySql Server the data is then consumed by Grafana for real-time analytics visualization. On a daily basis the data from MySql is appended to Hadoop File System with the help of Sqoop as the final storage space. The complete pipeline for transfer is automated by creating a pipeline and scheduling with the help of Airflow. 

## Data Flow : 
<img src = "https://github.com/RahieGadekar10/Store_Analytics_Grafana/blob/dee4aa3bb36213f9593b448ded4466a0bddfbcb3/sqoop.png"></img>

## Requirements : 
- Hadoop
- Sqoop
- Mysql
- Airflow for scheduling

## Deploying Model 

- Download the github repository using : 
  ```bash
  HTTPS : https://github.com/RahieGadekar10/Store_Analytics_Grafana.git
  ```
  ```bash 
  SSH : git@github.com:RahieGadekar10/Store_Analytics_Grafana.git
  ```
  ```bash 
  Github CLI : gh repo clone RahieGadekar10/Store_Analytics_Grafana
  ```
- To execute the project : 
 ```bash
Start Zookeeper and Kafka Server
```
- Start Producer
 ```bash
spark-submit spark_producer_new.py 
```
- Start Consumer
 ```bash
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.1 spark_consumer_new.py
```
## Scheduled Execution
- DAG code is present in sqoop_dag.py
```bash
start airflow webserver
start airflow scheduler
Goto Airflow webserver
```
- DAG will be present by the name sqoop_dag
- Run/Schedule the DAG to execute prediction operation.
