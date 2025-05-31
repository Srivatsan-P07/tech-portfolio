from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number, rank

spark = SparkSession.builder \
        .appName('sort-order-window') \
        .getOrCreate()

spark.sparkContext.setLogLevel('ERROR')

df1 = spark.read.csv('mock_data_7.csv', header = True, inferSchema = True)

# Sort
df1.sort('department').show()

# window orderby rownumber
window_spec = Window.orderBy(df1.salary.desc(), 'hire_date')
df1.withColumn(
    'salary_rank',
    row_number().over(window_spec)
).show()

# window partition rank
window_spec = Window.partitionBy('department').orderBy(df1.salary.desc(), 'hire_date')
df1.withColumn(
    'dept_rank',
    rank().over(window_spec)
) \
.filter('dept_rank == 1') \
.show()