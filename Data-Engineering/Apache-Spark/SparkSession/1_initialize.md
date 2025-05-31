
# 🧪 Initialize `SparkSession` (PySpark)

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MySparkApp") \
    .getOrCreate()
```
---
#### 📥 Basic Read/Write CSV in Spark

**Read CSV:**

```python
df = spark.read.csv("data.csv", header=True, inferSchema=True)
df.show()
```

**Write CSV:**

```python
df.write.csv("output_path", header=True)
```

---

Let me know if you want a simple hands-on example or a diagram to go with this!
