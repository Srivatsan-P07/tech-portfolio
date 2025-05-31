# **4️⃣ Data Cleaning & Transformation** in  **PySpark**

---

## 🔹 1. `na.drop()` – Dropping Nulls

Used to remove rows with **null (missing)** values from a DataFrame.

### 👉 Syntax:

```python
df.na.drop()
```

### 🧠 Options:

* `how="any"` – drop if **any column** is null (default)
* `how="all"` – drop if **all columns** are null
* `subset=["col1", "col2"]` – only check specific columns

### ✅ Example:

```python
df_cleaned = df.na.drop(how="any", subset=["age", "salary"])
```

---

## 🔹 2. `na.fill()` – Filling Nulls

Used to **replace null values** with specified defaults.

### 👉 Syntax:

```python
df.na.fill(value)
```

### 🧠 Options:

* Fill **all columns** with one value
* Pass a **dict** to specify different values per column

### ✅ Example:

```python
df_filled = df.na.fill({"age": 0, "name": "Unknown"})
```

---

## 🔹 3. Casting Types – `cast()`

Used to  **convert column data types** , especially important before aggregations, joins, etc.

### 👉 Syntax:

```python
from pyspark.sql.functions import col

df = df.withColumn("age", col("age").cast("integer"))
```

### 🧠 Common types:

* `"string"`
* `"int"` / `"integer"`
* `"float"`
* `"double"`
* `"boolean"`
* `"date"`

---

## 🔹 4. String Operations

PySpark has **tons** of functions to clean and manipulate strings.

### 👉 Common Functions:

* `lower()` / `upper()` – case conversion
* `trim()` – remove leading/trailing whitespace
* `regexp_replace()` – regex-based replacement
* `substring()` – extract substring
* `concat()` – join columns
* `split()` – split string into array

### ✅ Examples:

```python
from pyspark.sql.functions import col, lower, trim, regexp_replace

df = df.withColumn("name", lower(trim(col("name"))))
df = df.withColumn("name", regexp_replace(col("name"), "[^a-zA-Z ]", ""))
```

---

## 🔄 Summary:

| Action           | Method                                          |
| ---------------- | ----------------------------------------------- |
| Drop nulls       | `df.na.drop()`                                |
| Fill nulls       | `df.na.fill()`                                |
| Change data type | `col("colname").cast("type")`                 |
| String cleaning  | `lower()`,`trim()`,`regexp_replace()`etc. |

.
