# Amex PySpark Interview Questions

## Top 5 Detailed PySpark Questions

### 1. How do you handle data skewness in a join?
**Answer:** Use salting to spread skewed keys across partitions or use a broadcast join when one table is small.
- Salting: add a random suffix to the join key in both datasets, join on salted key, then remove salt.
- Broadcast join: use `broadcast(small_df)` to replicate the smaller table to every executor.
**Mistake:** Increasing resources without addressing the skew in data distribution.

### 2. Broadcast variables vs Accumulators.
**Answer:** Broadcast variables are read-only caches on workers used for lookups; accumulators are write-only counters or sums updated by workers and read by the driver.
**Follow-up:** Workers cannot reliably read accumulator values during task execution.

### 3. Repartition vs Coalesce.
**Answer:** `repartition()` reshuffles data and can increase or decrease partitions for even distribution. `coalesce()` avoids a full shuffle and only decreases the number of partitions by merging existing ones.
**Use case:** `repartition()` after a heavy filter to evenly balance partitions; `coalesce()` when reducing partition count on a stable dataset.

### 4. Explain the Catalyst Optimizer.
**Answer:** Spark parses the query, resolves column references, applies logical optimizations (predicate pushdown, constant folding), generates physical plans, chooses the cheapest plan, and produces optimized execution code.
**Mistake:** Assuming Spark executes Python code line by line rather than optimizing the query first.

### 5. How to handle Out of Memory (OOM) errors in Spark?
**Answer:** Profile the query, inspect skew, tune partition counts, broadcast small lookup tables, avoid `collect()` on large datasets, and tune Spark memory configs.
**Follow-up:** Driver OOM is different from executor OOM; driver OOM affects the job coordinator, while executor OOM affects tasks.

## Rapid-Fire PySpark Questions with Answers

6. Transformations vs Actions.
**Answer:** Transformations build lazy execution plans; actions trigger execution and return results.

7. Wide vs Narrow dependencies.
**Answer:** Narrow dependencies do not require shuffle (e.g., `map()`); wide dependencies require shuffle (e.g., `reduceByKey()`).

8. DAG (Directed Acyclic Graph) in Spark.
**Answer:** Spark creates a DAG of stages from transformations and executes it when an action is called.

9. RDD vs DataFrame vs Dataset.
**Answer:** RDD is low-level and untyped, DataFrame is optimized with schema, Dataset adds type safety in Scala.

10. Spark UI interpretation.
**Answer:** Use the Spark UI to inspect jobs, stages, tasks, shuffle behavior, and executor memory usage.

11. Tungsten execution engine.
**Answer:** Tungsten improves speed through bytecode generation, cache-aware memory management, and off-heap storage.

12. Memory overhead configuration.
**Answer:** Configure `spark.executor.memory`, `spark.driver.memory`, and memory fractions like `spark.memory.fraction`.

13. Reading/Writing Parquet vs ORC.
**Answer:** Both are columnar formats; Parquet is common and supports nested types, ORC often has better compression and performance for Hive workloads.

14. Handling corrupted records.
**Answer:** Use options like `badRecordsPath`, `mode='PERMISSIVE'`, or `mode='DROPMALFORMED'` when reading files.

15. UDFs vs Pandas/Vectorized UDFs.
**Answer:** Standard UDFs are slower because they serialize row-by-row; vectorized UDFs process batches and are faster.

16. Window functions in PySpark.
**Answer:** Use `Window.partitionBy(...).orderBy(...)` and functions like `row_number(), lag(), lead(), avg()`.

17. Join strategies (SortMerge, Broadcast, ShuffleHash).
**Answer:** Spark chooses based on data size and partitioning; broadcast joins avoid shuffle for small tables.

18. Checkpointing vs Caching.
**Answer:** Caching keeps data in memory for reuse; checkpointing writes data to durable storage to truncate lineage.

19. `cache()` vs `persist()`.
**Answer:** `cache()` is shorthand for `persist(StorageLevel.MEMORY_ONLY)`; `persist()` supports custom storage levels.

20. Watermarking in Spark Structured Streaming.
**Answer:** Watermarks allow handling late data by specifying how long to wait for delayed events.

21. Triggering batch vs streaming.
**Answer:** Batch runs once; streaming uses continuous triggers like `processingTime`.

22. Kafka integration with PySpark.
**Answer:** Use `spark.readStream.format('kafka')` or `writeStream.format('kafka')` with bootstrap servers and topic configs.

23. Handling small file problem on write.
**Answer:** Repartition before writing or use `coalesce()` to reduce file count.

24. Schema evolution.
**Answer:** Use schema merge or explicit schema updates when reading and writing formats like Parquet or Delta.

25. Dynamic partition pruning.
**Answer:** Spark can prune partitions at runtime using join filter values to reduce read volume.

26. Adaptive Query Execution (AQE).
**Answer:** AQE optimizes joins and shuffle partitions at runtime based on actual data statistics.

27. Filtering with `isin`.
**Answer:** Use `df.filter(col('x').isin(list_of_values))` for set membership filters.

28. Extracting nested JSON structures.
**Answer:** Use `from_json()`, `getItem()`, or dot notation on structs and arrays.

29. Exploding arrays.
**Answer:** Use `explode()` or `posexplode()` to convert array values into separate rows.

30. Deduplication (`dropDuplicates`).
**Answer:** Use `df.dropDuplicates(subset=['cols'])` or `row_number()` over partitions to keep one row.

31. Time travel in Delta Lake / Iceberg.
**Answer:** Use snapshot versions or timestamps to query historical table state.

32. `reduceByKey` vs `groupByKey`.
**Answer:** `reduceByKey` aggregates locally before shuffle, generally more efficient than `groupByKey`.

33. Serialization (Java vs Kryo).
**Answer:** Kryo is faster and more compact than Java serialization when configured properly.

34. Handling late-arriving data.
**Answer:** Use event-time processing with watermarks and appropriate windowing.

35. Z-Ordering for performance.
**Answer:** Use Z-order clustering (Delta Lake) to co-locate related data for faster selective reads.

36. Spark Submit parameters.
**Answer:** Configure `--master`, `--deploy-mode`, `--executor-memory`, `--num-executors`, and `--conf` values.

37. PySpark vs Scala Spark performance.
**Answer:** PySpark has a Python wrapper overhead, but performance is similar for DataFrame operations; Scala can be better for low-level RDD and typed logic.

38. Speculative execution.
**Answer:** Enables slow tasks to be re-launched as backups to reduce straggler impact.

39. Reading from RDBMS via JDBC in parallel.
**Answer:** Use partitioning options like `partitionColumn`, `lowerBound`, `upperBound`, and `numPartitions`.

40. Writing to BigQuery from PySpark.
**Answer:** Use the BigQuery Spark connector with `format('bigquery')` and destination table options.

41. Bloom filters in PySpark.
**Answer:** Use Bloom filters for approximate membership tests to reduce data scanned during joins.

42. State management in streaming.
**Answer:** Use stateful operations like `mapGroupsWithState()` or `flatMapGroupsWithState()`.

43. `map` vs `flatMap`.
**Answer:** `map()` returns one output row per input; `flatMap()` can return zero or more rows.

44. Handling `NULL`s in aggregation.
**Answer:** Use `coalesce()`, `na.fill()`, or aggregation functions that ignore nulls like `sum()`.

45. DataFrame column renaming and casting.
**Answer:** Use `withColumnRenamed()` and `cast()` to adjust schema.

46. `withColumn` performance implications.
**Answer:** `withColumn()` can add a new column and may recompute expressions if used repeatedly; chain carefully.

47. Joining streams with static data.
**Answer:** Use stream-static join semantics; ensure static data is small or broadcastable.

48. Graceful shutdown of streaming apps.
**Answer:** Use termination signals and `spark.streams.awaitAnyTermination()` with proper stop handling.

49. Unit testing PySpark code.
**Answer:** Use `pyspark.sql.SparkSession.builder.master('local[*]').getOrCreate()` and frameworks like `pytest`.

50. Difference between client and cluster deploy modes.
**Answer:** In client mode the driver runs on the submit machine; in cluster mode the driver runs on a worker node within the cluster.
