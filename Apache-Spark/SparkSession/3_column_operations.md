# **3️⃣ Column Operations in DataFrames**

When you're working with Spark DataFrames, most of the action happens through **column operations** — selecting, filtering, transforming, and renaming columns.

---

### 🔹 **Selecting Columns**

To grab one or more columns:

```python
df.select("name", "age").show()
```

You can also use the DataFrame API for more complex expressions:

```python
from pyspark.sql.functions import col

df.select(col("salary") * 1.1).show()
```

---

### 🔹 **Filtering Rows**

You can filter rows using `.filter()` or `.where()`:

```python
df.filter(df.age > 30).show()
```

Or using the `col()` function:

```python
df.filter(col("age") > 30).show()
```

Both `.filter()` and `.where()` are interchangeable.

---

### 🔹 **Adding New Columns (`withColumn`)**

Use `.withColumn()` to create a new column or modify an existing one:

```python
df = df.withColumn("new_salary", col("salary") * 1.1)
```

This doesn’t change the original DataFrame — it returns a **new one** with the extra column.

---

### 🔹 **Renaming Columns**

Use `.withColumnRenamed()` to rename columns:

```python
df = df.withColumnRenamed("name", "full_name")
```

If you need to rename multiple columns:

```python
df = df.withColumnRenamed("name", "full_name")\
       .withColumnRenamed("age", "years_old")
```

---

💡 **TL;DR**

| Operation  | Example                                |
| ---------- | -------------------------------------- |
| Select     | `df.select("name")`                  |
| Filter     | `df.filter(df.age > 30)`             |
| Add Column | `df.withColumn("new", col("x") * 2)` |
| Rename     | `df.withColumnRenamed("old", "new")` |

.
