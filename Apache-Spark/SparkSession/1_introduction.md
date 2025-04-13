**1️⃣ Introduction to Spark & SparkSession**

#### 🔥 What is  **Apache Spark** ?

Apache Spark is an **open-source distributed computing system** used for big data processing and analytics. It allows you to process large datasets **quickly** across many computers (clusters).

* Spark is written in  **Scala** , but it has APIs for  **Python (PySpark)** , Java, and R.
* It's **faster** than traditional MapReduce because it keeps data in **memory** (RAM) when possible.

---

#### 🧠 SparkSession vs SparkContext

 **SparkContext** :

* The original entry point into Spark.
* It represents the  **connection to a Spark cluster** .
* Used in earlier versions of Spark (before 2.0).

 **SparkSession** :

* Introduced in  **Spark 2.0** .
* It **encapsulates** both the `SparkContext` and `SQLContext`, making it easier to use.
* It's now the **default starting point** for all Spark functionality.

✅ Use `SparkSession` in modern Spark apps.

---

#### 🐌 Lazy Evaluation

Spark uses **lazy evaluation** — it doesn't compute anything until an **action** (like `collect()` or `show()`) is called.

* This allows Spark to  **optimize the entire execution plan** .
* Transformations (like `map`, `filter`, `select`) are  **lazy** .
* Actions (like `count`, `show`, `save`) trigger actual computation.

---

#### 🏗️ Spark Architecture (High-Level)

* **Driver** : The main program (your code) that defines the transformations/actions.
* **Cluster Manager** : Allocates resources (like YARN, Mesos, Kubernetes, or standalone).
* **Executors** : Run on worker nodes and actually perform computations.

Flow:

```
Driver → Cluster Manager → Executors → Results back to Driver
```
