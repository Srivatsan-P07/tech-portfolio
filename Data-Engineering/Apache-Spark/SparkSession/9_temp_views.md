# **SQL with SparkSession**

In  **Apache Spark** , especially when using  **PySpark (Python API for Spark)** , you can write **SQL queries** to process and analyze data. This is done using a  **`SparkSession`** , which is the entry point to work with DataFrames and SQL in Spark.

#### **1. Registering Temp Views**

Before you can run SQL queries on a DataFrame, you need to  **register it as a temporary view** :

```python
df.createOrReplaceTempView("my_table")
```

This line does two things:

* **Creates a temporary view** called `"my_table"` from the DataFrame `df`.
* This view is accessible within that SparkSession using SQL.

You can also use `createGlobalTempView("my_table")` if you want the view to persist across sessions (it’ll be in the `global_temp` database).

#### **2. Running SQL Queries**

Once the view is registered, you can write SQL queries as if you're querying a SQL table:

```python
result = spark.sql("SELECT * FROM my_table WHERE age > 30")
result.show()
```

This:

* Executes the SQL query on the temporary view.
* Returns the result as a  **new DataFrame** .
* You can then use all DataFrame operations on `result`.

.