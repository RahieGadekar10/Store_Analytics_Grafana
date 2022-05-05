from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql import functions
import sqlalchemy
import pandas as pd
class Consumer:
    def __init__(self):
        self.spark =SparkSession.builder.master("local").appName("NewProject").config("spark.jars.package","org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.1").config("spark.ui.port","4041").getOrCreate()

    def process_each_record(self, df, epoch_id):

        df = df.select("orderdate","shipmode","segment","country","city","state","region","category","subcategory","sales","quantity","profit","timestamp")
        df = df.toPandas()
        self.insert_to_sql(df=df)

    def insert_to_sql(self, df):
        df.to_csv("new1.csv")
        engine = sqlalchemy.create_engine("mysql+pymysql://rahie:rahie@localhost:3306/sqoopdatabase")
        df.to_sql(con=engine, name='store', if_exists='append', index=False)

    def consume(self):
        schema= "orderdate date ,shipmode string ,segment string,country string,city string,state string,region string,category string,subcategory string,sales double,quantity int,profit double"
        dataframe = self.spark.readStream.format("kafka").option("kafka.bootstrap.servers",'localhost:9092').option("subscribe","newtopic").option("startingOffsets","latest").load()
        dataframe1 = dataframe.selectExpr("CAST(value as STRING)","timestamp")
        dataframe2 = dataframe1.select(from_csv(functions.col("value"), schema).alias("records"),"timestamp")
        dataframe3 = dataframe2.select("records.*","timestamp")
        transformed_df = dataframe3
        query = transformed_df.writeStream.format("console").trigger(processingTime="5 seconds").foreachBatch(self.process_each_record).start()
        query.awaitTermination()

def main() :
    kafkaconsumer = Consumer()
    kafkaconsumer.consume()

if __name__ == "__main__" :
    main()


