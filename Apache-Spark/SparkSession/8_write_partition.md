# Spark Output

* Writing to  **CSV** ,  **Parquet** , **JSON**
* **Partitioning** data when saving

We'll assume you already have a Spark session like this:

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DataIO").getOrCreate()
```

---

### 🔹1. **Writing Data**

Suppose you have a DataFrame called `df`:

```python
df = spark.read.csv("path/to/input.csv", header=True, inferSchema=True)
```

#### ➤ Write to CSV

```python
df.write.csv("path/to/output_csv", header=True, mode="overwrite")
```

#### ➤ Write to Parquet (efficient, columnar format)

```python
df.write.parquet("path/to/output_parquet", mode="overwrite")
```

#### ➤ Write to JSON

```python
df.write.json("path/to/output_json", mode="overwrite")
```

📌 `mode` can be:

* `"overwrite"` – replace existing files
* `"append"` – add to existing
* `"ignore"` – do nothing if exists
* `"error"` or `"errorifexists"` – (default) throws error if exists

---

### 🔹2. **Partitioning Data on Write**

You can organize data into folders based on column values:

#### ➤ Example: Partition by `year` and `month`

```python
df.write.partitionBy("year", "month").parquet("path/to/partitioned_output", mode="overwrite")
```

This will save the files like:

```
path/to/partitioned_output/year=2023/month=04/
path/to/partitioned_output/year=2023/month=05/
...
```

Partitioning is especially useful for efficient filtering and query performance in big data.

---

.
