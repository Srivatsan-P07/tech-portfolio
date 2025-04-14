from pyspark.sql import SparkSession
from pyspark.sql.functions import count, avg

spark = SparkSession.builder.appName('cleaning-transformation').getOrCreate()
spark.sparkContext.setLogLevel('ERROR')

df = spark.read.csv('mock_data.csv', header = True, inferSchema = True)
modified_df = df.na.drop(how='any')

grouped_df = modified_df.groupBy('city').agg(
    count("*").alias("count"),
    avg("salary").alias("average_salary")
)

grouped_df.show()