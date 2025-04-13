# RDDs (Resilient Distributed Datasets)**

**RDDs** are the core abstraction in **Apache Spark**. They represent **immutable, distributed collections of objects** that can be processed in parallel across a cluster. RDDs allow Spark to handle large-scale data processing with fault tolerance and high performance.

---

#### ✅ **1. Creation**
You can create RDDs in two main ways:
- **From existing data in storage**: e.g., reading from HDFS, S3, local file systems
  ```python
  rdd = spark.sparkContext.textFile("data.txt")
  ```
- **From existing collections in your program** (for testing or small datasets):
  ```python
  rdd = spark.sparkContext.parallelize([1, 2, 3, 4])
  ```

---

#### 🔄 **2. Transformations**
Transformations are operations on RDDs that return a **new RDD**. They are **lazy**, meaning they are only computed when an action is called.

- **Examples**:
  - `map()`: apply a function to each element
  - `filter()`: filter elements based on a condition
  - `flatMap()`: flatten results after mapping
  - `distinct()`, `union()`, `join()`, etc.

  ```python
  rdd2 = rdd.map(lambda x: x * 2)
  ```

---

#### ✅ **3. Actions**
Actions trigger the **actual execution** of the transformations and return results.

- **Examples**:
  - `collect()`: return all elements as a list
  - `count()`: count number of elements
  - `first()`, `take(n)`, `reduce()`, `saveAsTextFile()`, etc.

  ```python
  total = rdd.reduce(lambda a, b: a + b)
  ```

---

#### 🧠 **4. Persistence and Caching**
To avoid recomputation of RDDs during multiple actions, Spark allows you to **persist** (store) them in memory or on disk.

- **cache()**: stores RDD in memory
- **persist()**: more control (e.g., memory and/or disk)

  ```python
  rdd.cache()  # or rdd.persist(StorageLevel.DISK_ONLY)
  ```

This is **especially useful** when the RDD is reused multiple times.