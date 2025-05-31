from pyspark.sql import SparkSession

spark = SparkSession.builder \
        .appName('joins-in-spark') \
        .getOrCreate()

spark.sparkContext.setLogLevel('ERROR')

df1 = spark.read.csv('join_data_1.csv', header = True, inferSchema = True)
df2 = spark.read.csv('join_data_2.csv', header = True, inferSchema = True)

print('----- inner join -----')
df1.join(df2, df1.user_id == df2.user_id, how='inner').show()

print('----- left join -----')
df1.join(df2, df1.user_id == df2.user_id, how='left').show()

print('----- right join -----')
df1.join(df2, df1.user_id == df2.user_id, how='right').show()

print('----- outer join -----')
df1.join(df2, df1.user_id == df2.user_id, how='outer').show()