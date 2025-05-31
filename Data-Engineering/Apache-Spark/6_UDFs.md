# UDFs in Spark

A **User Defined Function (UDF)** in Spark allows you to define **custom logic** and apply it to  **DataFrame columns** —either through **PySpark code** or  **SQL queries** .

---

## 🔸 PySpark UDF (Using Python Code)

### ✅ Steps:

1. Define a regular Python function.
2. Convert it into a UDF using `pyspark.sql.functions.udf()`.
3. Use it in a DataFrame transformation.

### 💡 Example:

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

# Start Spark session
spark = SparkSession.builder.appName("UDF Example").getOrCreate()

# Sample DataFrame
data = [("alice",), ("bob",)]
df = spark.createDataFrame(data, ["name"])

# Step 1: Define Python function
def to_upper(s):
    return s.upper() if s else None

# Step 2: Register UDF
to_upper_udf = udf(to_upper, StringType())

# Step 3: Use it in DataFrame
df_with_upper = df.withColumn("name_upper", to_upper_udf(df["name"]))
df_with_upper.show()
```

**🧾 Output:**

```
+-----+-----------+
| name|name_upper |
+-----+-----------+
|alice|ALICE      |
|bob  |BOB        |
+-----+-----------+
```

---

## 🔸 Spark SQL UDF (Using SQL Query)

### ✅ Steps:

1. Define and register the UDF.
2. Create a temporary view of your DataFrame.
3. Call the UDF inside an SQL query.

### 💡 Example (continued from above):

```python
# Step 1: Register the UDF with SQL name
spark.udf.register("to_upper_sql", to_upper, StringType())

# Step 2: Create a SQL temporary view
df.createOrReplaceTempView("people")

# Step 3: Use it in SQL
result = spark.sql("SELECT name, to_upper_sql(name) AS name_upper FROM people")
result.show()
```

**🧾 Output:**

```
+-----+-----------+
| name|name_upper |
+-----+-----------+
|alice|ALICE      |
|bob  |BOB        |
+-----+-----------+
```

---

## 🔍 Key Notes:

| Feature      | PySpark UDF                     | Spark SQL UDF                             |
| ------------ | ------------------------------- | ----------------------------------------- |
| Used In      | DataFrame API (`withColumn`)  | SQL queries (`spark.sql()`)             |
| Registration | Optional for DataFrame          | Required for SQL (`spark.udf.register`) |
| Performance  | Slower than built-in functions  | Same performance caveat                   |
| Type Safety  | You define return type manually | Same                                      |

---

.
