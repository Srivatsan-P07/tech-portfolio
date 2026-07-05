Here’s the complete checklist for optimizing / handling skewed joins in [BigQuery](https://cloud.google.com/bigquery?utm_source=chatgpt.com):

* **Partition large tables** on frequently filtered `DATE/TIMESTAMP` columns
  → partition pruning, less scan
* **Cluster on frequently filtered / joined high-cardinality columns**
  → e.g. `user_id`, `customer_id`, `device_id`
* **Filter early, join later**
  → reduce rows before shuffle
* **Pre-aggregate before joins**
  → `GROUP BY` first if possible
* **Join small tables first / leverage broadcast joins**
  → reduce network movement
* **Do biggest joins last**
  → after reducing dataset size
* **Avoid `SELECT *`**
  → BigQuery is columnar ( **Dremel** ) so scan only needed columns
* **Check query execution plan / bytes scanned / bytes shuffled**
  → identify bottlenecks
* **Identify skewed join keys**
  → detect hot keys with highly uneven distribution
* **Use salting for severe skew**
  → manually distribute hot keys across buckets
  (BigQuery does **not** auto-salt)
* **Use materialized views / summary tables**
  → avoid repeated expensive computation
* **Use approximate aggregations when acceptable**
  → e.g. `APPROX_COUNT_DISTINCT`
* **Avoid repeated CTE evaluation**
  → BigQuery may re-execute CTEs
* **Denormalize when sensible**
  → nested/repeated fields can reduce joins
* **Always use partition filters explicitly**
  → avoid accidental full table scans
