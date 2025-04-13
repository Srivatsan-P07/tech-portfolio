# 5️⃣ **Aggregation & GroupBy in PySpark**

Aggregation is used to **summarize data** — like finding totals, averages, or counts grouped by a specific column (like category, department, or city).

---

### 🔧 Common Aggregation Functions

| Function    | Description          |
| ----------- | -------------------- |
| `count()` | Count number of rows |
| `sum()`   | Sum of values        |
| `avg()`   | Average              |
| `max()`   | Maximum              |
| `min()`   | Minimum              |

These are available under `pyspark.sql.functions`.

---

## 🧪 Example 1: Simple `groupBy().agg()`

```python
from pyspark.sql.functions import avg, count, sum

df.groupBy("city").agg(
    count("*").alias("total_people"),
    avg("salary").alias("avg_salary"),
    sum("salary").alias("total_salary")
).show()
```

👉 This groups the DataFrame by `city` and:

* Counts how many people are in each city
* Calculates the average salary
* Calculates the total salary

---

## 🧪 Example 2: Aggregating Without Grouping

You can aggregate the whole dataset:

```python
df.agg(
    avg("salary").alias("avg_salary"),
    count("*").alias("total_rows")
).show()
```

---

## ✅ Quick Notes:

* `groupBy()` is always followed by `.agg()` or an aggregation function
* You can use multiple aggregations at once
* Always import aggregation functions from `pyspark.sql.functions`

---

### 🧠 Real Example:

Say you want to get average age and count of employees in each department:

```python
df.groupBy("department").agg(
    avg("age").alias("avg_age"),
    count("*").alias("num_employees")
).show()
```

---

.
