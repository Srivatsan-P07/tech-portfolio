# Explain the architecture of Apache Spark (Driver, Executors, Cluster Manager)

```text
Apache Spark follows a master-worker architecture:

• Driver:
  - Main process running the Spark application.
  - Creates SparkSession/SparkContext.
  - Converts user code into execution plans (DAGs).
  - Schedules tasks across executors.

• Executors:
  - Worker processes running on cluster nodes.
  - Execute tasks assigned by driver.
  - Store data in memory/disk for caching.
  - Return results to driver.

• Cluster Manager:
  - Allocates resources for Spark apps.
  - Examples: Standalone, YARN, Mesos, Kubernetes.

Flow:
User Code → Driver → Cluster Manager allocates Executors → Executors process tasks
```

# What is a Resilient Distributed Dataset (RDD)?

```text
RDD is Spark’s fundamental distributed data structure.

Properties:
• Resilient → Fault tolerant via lineage (can recompute lost partitions)
• Distributed → Partitioned across nodes
• Immutable → Cannot modify in-place
• Lazy → Operations execute only when action is called

RDDs are low-level APIs used for fine-grained distributed processing.
```

# What is the difference between transformations and actions in PySpark?

```text
Transformations:
• Create new datasets from existing ones
• Lazy (not executed immediately)
• Examples: map(), filter(), select()

Actions:
• Trigger execution and return result / write output
• Examples: collect(), count(), show(), save()

Example:
df.filter(col("age") > 18)   → Transformation
df.count()                   → Action
```

# Explain the differences between Spark DataFrames and RDDs

```text
RDD:
• Low-level API
• Stores objects
• No schema
• More flexible, less optimized

DataFrame:
• High-level structured API
• Tabular data with schema
• Optimized by Catalyst + Tungsten
• Faster for SQL-style workloads

Use RDD:
• Complex custom transformations

Use DataFrame:
• Most production workloads
```

# Explain the concept of lazy evaluation in Spark

```text
Spark delays execution until an action is called.

Example:
df = spark.read.csv(...)
df = df.filter(...)
df = df.select(...)

Nothing runs yet.

Only when:
df.show()

Spark builds an optimized execution plan and runs it.

Benefits:
• Optimization
• Reduced computation
• Pipeline fusion
```

# Explain narrow vs. wide dependencies in Spark

```text
Narrow Dependency:
• Child partition depends on one parent partition
• No shuffle needed
• Faster

Examples:
map(), filter()

Wide Dependency:
• Child partition depends on multiple parent partitions
• Shuffle required
• Slower

Examples:
groupBy(), join(), reduceByKey()
```

# How does Spark handle shuffling, and why is it an expensive operation?

```text
Shuffle redistributes data across partitions.

Example:
groupBy("dept")

Process:
1. Map-side tasks write intermediate data
2. Data transferred across network
3. Reduce-side tasks read data

Why expensive?
• Disk I/O
• Network transfer
• Serialization/deserialization
• Memory pressure

Shuffle is often the biggest bottleneck.
```

# What is the difference between repartition() and coalesce()?

```text
repartition():
• Increases or decreases partitions
• Full shuffle
• Better balancing
• Expensive

coalesce():
• Usually decreases partitions
• Minimal shuffle
• Faster

Use:
repartition(200) → better distribution
coalesce(10)     → reduce partitions before write
```

# Explain how broadcasting works in Spark SQL

```text
Broadcasting sends a small dataset to all executors.

Used in joins:
Large Table JOIN Small Table

Instead of shuffling both tables:
• Small table copied to each executor
• Large table stays partitioned

Benefits:
• Avoids shuffle
• Faster joins

Example:
broadcast(dim_table)
```

# What is the difference between Dask and Spark? When would you use Dask over Spark?

```text
Spark:
• JVM-based
• Big-data ecosystem
• Excellent SQL/ETL
• Strong fault tolerance

Dask:
• Python-native
• Integrates with NumPy/Pandas
• Easier for Python ML workflows

Use Dask when:
• Mostly Python stack
• Pandas-like workflows
• Smaller clusters
• ML experimentation

Use Spark when:
• Huge distributed ETL
• Enterprise pipelines
```

# How do you write unit tests for Spark applications?

```text
Use testing frameworks like:
• pytest
• unittest

Approach:
1. Create local SparkSession
2. Build small test DataFrames
3. Apply transformation
4. Assert results

Example checks:
• Row count
• Schema
• Output values

Best practice:
Keep transformations in pure reusable functions.
```

# Describe the difference between cache() and persist() in PySpark

```text
cache():
• Shortcut for persist(MEMORY_ONLY)

persist():
• Allows storage level control

Storage levels:
• MEMORY_ONLY
• MEMORY_AND_DISK
• DISK_ONLY
• OFF_HEAP

Use cache:
• Fits in memory

Use persist:
• Large datasets / custom strategy
```

# How do you process nested JSON or Avro files using PySpark?

```text
JSON:
spark.read.json(path)

Nested fields:
• dot notation
• explode()
• select()

Example:
df.select("user.name")

Avro:
spark.read.format("avro").load(path)

Useful functions:
• explode()
• from_json()
• schema_of_json()

Goal:
Flatten nested structures for analytics.
```

# Discuss general Databricks and Spark architecture knowledge

```text
Databricks = Managed Spark platform.

Architecture:
• Control Plane:
  - UI
  - Notebook
  - Job scheduler
  - Cluster management

• Data Plane:
  - Spark clusters run here
  - User workloads execute here

Key Components:
• Driver node
• Worker nodes
• DBFS / cloud storage
• Delta Lake
• Unity Catalog
• Photon (vectorized engine)

Common concepts:
• Interactive clusters
• Job clusters
• Auto-scaling
• Lakehouse architecture
• Medallion layers:
  Bronze → Raw
  Silver → Cleaned
  Gold → Business-ready
```

# Describe how to optimize Spark jobs using broadcasting, partitioning, and caching

```text
Broadcasting:
• Broadcast small lookup tables
• Avoid shuffle joins

Partitioning:
• Partition by frequently filtered/joined columns
• Reduce skew and shuffle

Caching:
• Cache reused intermediate DataFrames
• Avoid recomputation

Also:
• Avoid wide transformations
• Use DataFrames over RDDs
• Tune spark.sql.shuffle.partitions
```

# How do you handle data skew in PySpark?

```text
Data skew happens when some partitions have much more data.

Solutions:
• Salting keys
• Broadcast small tables
• Repartition better
• Enable AQE skew join handling
• Filter skewed keys separately

Symptoms:
• Few tasks run much longer
• Executors idle waiting
```

# How does the Spark Catalyst Optimizer work?

```text
Catalyst optimizes DataFrame/SQL queries.

Stages:
1. Parsed Logical Plan
2. Analyzed Logical Plan
3. Optimized Logical Plan
4. Physical Plan

Optimizations:
• Predicate pushdown
• Constant folding
• Projection pruning
• Join reordering

Result:
Efficient execution plan
```

# How do you debug Out of Memory (OOM) errors in a Spark executor?

```text
Common causes:
• Large partitions
• Large shuffle
• collect() misuse
• Excess caching

Debug:
1. Check Spark UI
2. Inspect executor logs
3. Identify stage/task failing
4. Check skew/shuffle size

Fix:
• Increase executor memory
• Increase partitions
• Reduce shuffle
• Use MEMORY_AND_DISK
• Avoid collect()
```

# What is Adaptive Query Execution (AQE) in Spark 3.0?

```text
AQE dynamically optimizes query plans during runtime.

Features:
• Coalesce shuffle partitions
• Convert sort-merge join → broadcast join
• Handle skew joins

Why useful?
Initial estimates may be wrong.
AQE uses runtime statistics to improve execution.

Result:
Faster and more efficient jobs.
```

# Explain how checkpointing differs from caching in Spark

```text
Caching:
• Stores computed data in memory/disk
• Speeds repeated access
• Keeps lineage

Checkpointing:
• Saves data to reliable storage (HDFS/S3)
• Cuts lineage
• Improves fault recovery

Use cache:
• Performance optimization

Use checkpoint:
• Very long lineage / iterative algorithms
```
