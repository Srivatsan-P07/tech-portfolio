from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import time

spark = SparkSession.builder \
        .appName('1-Initialization') \
        .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

df = spark.read.csv("data.csv", header = True, inferSchema = True)

df.printSchema()

df.select('name', 'profession').show()
df.filter(df.age > 25).show()
df.filter(col('age') == 25).show()