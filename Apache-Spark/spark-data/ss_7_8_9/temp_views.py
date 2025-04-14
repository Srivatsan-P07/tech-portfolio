from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('temp-view').getOrCreate()
spark.sparkContext.setLogLevel('ERROR')

df = spark.read.parquet('parquet_output')

df.createOrReplaceTempView('emp_data')
df.createOrReplaceGlobalTempView('global_emp_data')

# temp sql
spark.sql(
    """
    SELECT 
        first_name || ' ' || last_name AS name, 
        salary 
    FROM 
        emp_data 
    ORDER BY 
        salary DESC
    """
).show()

#Global Temp referenced sql
spark.sql(
    """
    SELECT 
        first_name || ' ' || last_name AS name, 
        hire_date 
    FROM 
        global_temp.global_emp_data
    ORDER BY 
        hire_date DESC
    """
).show()