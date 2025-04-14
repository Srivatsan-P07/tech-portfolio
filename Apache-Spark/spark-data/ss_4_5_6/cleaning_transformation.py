from pyspark.sql import SparkSession
from pyspark.sql.functions import col, upper, trim

spark = SparkSession.builder.appName('cleaning-transformation').getOrCreate()
spark.sparkContext.setLogLevel('ERROR')

df = spark.read.csv('mock_data.csv', header = True, inferSchema = True)
df.show()


# Drop Nulls
print('----- Drop Nulls -----')
drop_1 = df.na.drop()
drop_1.show()

drop_2 = df.na.drop(how='all', subset=['age', 'salary'])
drop_2.show()

drop_3 = df.na.drop(how='any', subset=['age', 'salary'])
drop_3.show()

# Fill Nulls
print('----- Fill Nulls -----')

df2 = spark.read.csv('mock_data.csv', header = True, inferSchema = True)
df2.printSchema()

filler = {
    "name" : "unknown",
    "age" : 0,
    "salary" : 0.0,
    "city" : "unknown"
}
fill_1 = df2.na.fill(filler) # Different data type cannot handle nulls without null filler dictionary
fill_1.show()

# Type Casting

new_salary_df = drop_3.withColumn( "salary", col("salary").cast('integer') ) #giving same column name will replace the column
new_salary_df.show()

# String Operations

new_df = fill_1.withColumn("name", upper(trim("name"))) \
            .withColumn("city", upper(trim("city")))

new_df.show()