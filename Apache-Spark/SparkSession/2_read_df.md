
### **2️⃣ Working with DataFrames**

In Spark (or PySpark), **DataFrames** are a core abstraction for working with structured and semi-structured data. Think of them like super-powered spreadsheets or SQL tables.

---

### ✅ **Reading from CSV/JSON/Parquet**

You can load data into DataFrames from various sources like:

#### 🟡 CSV

```python
df = spark.read.csv("file.csv", header=True, inferSchema=True)
```

#### 🟠 JSON

```python
df = spark.read.json("file.json")
```

#### 🟢 Parquet (a columnar storage format, very efficient)

```python
df = spark.read.parquet("file.parquet")
```

* `inferSchema=True`: Tries to guess the data types automatically. This helps Spark optimize queries.
* `header=True`: Uses the first row as column names (only for CSVs).

---

### 📋 **Useful DataFrame Methods**

#### `.show()`

Displays the top 20 rows of the DataFrame in a tabular format.

```python
df.show()
```

#### `.printSchema()`

Prints the inferred schema in a tree-like structure.

```python
df.printSchema()
```

.
