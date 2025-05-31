from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('write-output').getOrCreate()
spark.sparkContext.setLogLevel('ERROR')

df = spark.read.csv('mock_data_7.csv', header = True, inferSchema = True)

df.write.csv('csv_output', header = True, mode = 'overwrite')
df.write.json('json_output', mode = 'overwrite')
df.write.parquet('parquet_output', mode = 'overwrite')
df.write.partitionBy('hire_date').parquet('partition_output', mode = 'overwrite')