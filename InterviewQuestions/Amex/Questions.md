Analysis of American Express Data Engineer Interviews
Structure (Typically 3 Rounds):
Round 1 (Technical): Live coding in SQL and Python. PySpark fundamentals, data structures, and algorithms (focus on strings, arrays, and dictionaries).
Round 2 (System Design & Projects): Deep dive into past projects. Architecture design on GCP, handling scale, performance tuning, and batch vs. streaming trade-offs.
Round 3 (Hiring Manager/Behavioral): Culture fit, scenario-based project management, stakeholder communication, and failure resolution.
Difficulty Level: Medium to Hard. Focuses heavily on practical application, optimization, and real-world edge cases over theoretical trivia.
Common Patterns:
Heavy emphasis on PySpark query optimization (handling skew, avoiding shuffles, broadcast joins).
SQL focuses on analytical queries (Window functions, recursive CTEs).
GCP focus is on selecting the right tool (Dataflow vs. Dataproc) and streaming architecture (Pub/Sub).
Highest ROI Topics (Focus Here First)
PySpark Optimization: Join strategies, partitioning techniques, addressing data skew, and understanding the Catalyst Optimizer.
Advanced SQL: Window functions (ranking, running totals, lead/lag) and recursive CTEs.
GCP Architecture: Streaming pipelines (Pub/Sub + Dataflow) vs. Batch processing (GCS + Dataproc + BigQuery).
Python Fundamentals: Data structures, file I/O, decorators, and memory management (generators vs iterators).
Idempotency: Designing pipelines that process data exactly once, handling duplicate data safely under failure conditions.
Preparation Schedule (3 Days Left)
Day 1 (Execution): SQL and Python. Practice Window Functions, CTEs, and LeetCode Medium string/array manipulation.
Day 2 (Big Data): PySpark internals and optimization. Understand RDDs vs DataFrames, transformations vs actions, and memory tuning.
Day 3 (Architecture & Fit): System Design (GCP focus) and Behavioral. Review past projects. Formulate STAR (Situation, Task, Action, Result) answers for production failures and team conflicts.
Adjust your study plan dynamically using the tool below based on the days remaining until your interview.




Detailed Question Bank
(Note: To maximize efficiency for a condensed timeline, the absolute highest-yield questions contain full breakdowns. The remainder are listed as rapid-fire concepts for your self-assessment).
Top 50 SQL Questions
Detailed Breakdown (Top 5):
Find the running total of transactions per customer.
Concept: Window functions (SUM() OVER()).
Answer: SELECT cust_id, txn_date, amount, SUM(amount) OVER(PARTITION BY cust_id ORDER BY txn_date) as running_total FROM transactions;
Follow-up: How does performance change if you remove ORDER BY?
Real-world: Tracking credit card balance limits in real-time.
Mistake: Forgetting the ORDER BY inside the OVER() clause, resulting in a total sum for the customer on every row instead of a running sum.
Find the 3rd highest salary in each department.
Concept: Ranking window functions.
Answer: Use DENSE_RANK() OVER(PARTITION BY dept_id ORDER BY salary DESC). Wrap in a CTE and filter for rank = 3.
Follow-up: Difference between RANK() and DENSE_RANK()?
Real-world: Identifying top spending merchants per category.
Mistake: Using RANK() which skips numbers on ties.
Identify gaps in sequential data (e.g., missing transaction IDs).
Concept: LEAD()/LAG().
Answer: Compare current ID with LAG(id) OVER (ORDER BY id). If the difference is > 1, there is a gap.
Follow-up: How to generate the actual missing numbers?
Real-world: Detecting dropped data packets or skipped invoice numbers.
Mistake: Not handling the first row (where LAG evaluates to null).
Find customers who bought both Product A and Product B.
Concept: Intersect or Conditional Aggregation.
Answer: SELECT cust_id FROM sales WHERE product IN ('A', 'B') GROUP BY cust_id HAVING COUNT(DISTINCT product) = 2;
Follow-up: How to scale this if checking for 50 specific products?
Real-world: Market basket analysis.
Mistake: Using a simple AND in the WHERE clause (e.g., product = 'A' AND product = 'B'), which returns no rows.
Calculate year-over-year growth per month.
Concept: Time-series aggregation and LAG().
Answer: Aggregate by month/year, then use LAG(revenue, 12) OVER(ORDER BY month_year) to get last year's revenue, calculate percentage change.
Follow-up: How do you handle months with zero revenue to avoid division by zero?
Real-world: Amex quarterly earnings reports.
Mistake: Joining the table to itself on a complex date manipulation instead of using cleaner window functions.
Rapid-Fire Concepts (45):
6. Recursive CTE for organizational hierarchy.
7. Pivot rows to columns without PIVOT function.
8. Unpivot columns to rows.
9. Delete duplicate rows keeping the lowest ID.
10. Moving average over 7 days.
11. First and last transaction per customer.
12. Customers who churned (no activity in 30 days).
13. Finding overlapping date ranges.
14. Cumulative distribution of sales.
15. Median salary calculation.
16. Join vs Union performance.
17. Cross join use cases.
18. Handling NULLs in NOT IN vs NOT EXISTS.
19. Optimizing queries with indexes.
20. Explain plans and execution paths.
21. Temporary tables vs CTEs.
22. Extracting JSON values in SQL.
23. Percentile calculations.
24. Identifying consecutive streaks.
25. Rollup vs Cube.
26. Updating a table based on a join.
27. Handling time zones.
28. Coalesce vs IsNull.
29. Exact vs Approximate distinct counts.
30. Finding the most frequent value (Mode).
31. String manipulation (Substring, Regex).
32. Date math (Days between dates).
33. Materialized views trade-offs.
34. Partitioning by date.
35. Clustered vs Non-clustered indexes.
36. Left Anti Join logic.
37. Grouping Sets.
38. Returning rows with maximum value per group without window functions.
39. Full outer join scenarios.
40. Case statements for categorical binning.
41. Calculating retention rate.
42. Sequence generation.
43. Upsert (Merge) statements.
44. Handling division by zero safely.
45. Comparing table schemas.
46. Finding orphaned records.
47. Querying hierarchical data without CTEs.
48. Triggers and stored procedures (concept).
49. Row-level security basics.
50. SQL injection prevention.

Top 50 PySpark Questions
Detailed Breakdown (Top 5):
How do you handle data skewness in a join?
Concept: Data skew causes straggler tasks and OOM issues.
Answer: Use salting (adding a random key to the skewed column to distribute it across partitions), or use Broadcast Hash Join if one table is small enough.
Follow-up: What happens if the salted table needs to be joined back to the original format?
Real-world: Joining a massive transactions table on a highly popular merchant ID.
Mistake: Just increasing resources/memory instead of fixing the logical skew.
Broadcast variables vs Accumulators.
Concept: Distributed shared variables.
Answer: Broadcast variables are read-only cached on worker nodes (lookups). Accumulators are write-only variables updated by workers (counters).
Follow-up: Can workers read accumulators? (No, only the driver can).
Real-world: Broadcasting a small lookup table of country codes; accumulating the count of malformed records.
Mistake: Trying to use accumulators for business logic control flow.
Repartition vs Coalesce.
Concept: Managing partition counts.
Answer: repartition() causes a full shuffle (can increase or decrease partitions). coalesce() minimizes shuffling but only decreases partitions by merging existing ones.
Follow-up: When would you use repartition over coalesce? (When you need evenly distributed data after heavy filtering).
Real-world: Writing a final dataset to storage to avoid the small file problem.
Mistake: Using repartition() to lower partition counts, causing unnecessary network I/O.
Explain the Catalyst Optimizer.
Concept: Spark's query execution engine.
Answer: It parses the query, analyzes it (resolves column names), logically optimizes it (predicate pushdown, constant folding), creates multiple physical plans, selects the cheapest via cost model, and generates execution code.
Follow-up: How does predicate pushdown work?
Real-world: Filtering data at the storage level (e.g., Parquet) before loading it into memory.
Mistake: Thinking Spark blindly executes code line-by-line in Python.
How to handle Out of Memory (OOM) errors in Spark?
Concept: Memory management and tuning.
Answer: Check for skewed data, increase partition count, tune memory fractions, ensure small tables are broadcasted, and avoid using collect() on large datasets.
Follow-up: Difference between Driver OOM and Executor OOM?
Real-world: Processing billions of Amex swipes daily.
Mistake: Automatically asking for larger compute instances without profiling the code.
Rapid-Fire Concepts (45):
6. Transformations vs Actions.
7. Wide vs Narrow dependencies.
8. DAG (Directed Acyclic Graph) in Spark.
9. RDD vs DataFrame vs Dataset.
10. Spark UI interpretation.
11. Tungsten execution engine.
12. Memory overhead configuration.
13. Reading/Writing Parquet vs ORC.
14. Handling corrupted records.
15. UDFs (User Defined Functions) vs Pandas/Vectorized UDFs.
16. Window functions in PySpark.
17. Join strategies (SortMerge, Broadcast, ShuffleHash).
18. Checkpointing vs Caching.
19. cache() vs persist().
20. Watermarking in Spark Structured Streaming.
21. Triggering batch vs streaming.
22. Kafka integration with PySpark.
23. Handling small file problem on write.
24. Schema evolution.
25. Dynamic partition pruning.
26. Adaptive Query Execution (AQE).
27. Filtering with isin.
28. Extracting nested JSON structures.
29. Exploding arrays.
30. Deduplication (dropDuplicates).
31. Time travel in Delta Lake / Iceberg.
32. reduceByKey vs groupByKey.
33. Serialization (Java vs Kryo).
34. Handling late-arriving data.
35. Z-Ordering for performance.
36. Spark Submit parameters.
37. PySpark vs Scala Spark performance.
38. Speculative execution.
39. Reading from RDBMS via JDBC in parallel.
40. Writing to BigQuery from PySpark.
41. Bloom filters in PySpark.
42. State management in streaming.
43. Map vs FlatMap.
44. Handling NULLs in aggregation.
45. DataFrame column renaming and casting.
46. withColumn performance implications.
47. Joining streams with static data.
48. Graceful shutdown of streaming apps.
49. Unit testing PySpark code.
50. Difference between client and cluster deploy modes.
Top 30 Python Questions
Detailed Breakdown (Top 3):
Generators vs Iterators.
Concept: Memory Management and Lazy Evaluation.
Answer: Generators yield values one at a time, minimizing memory usage. Iterators load the entire object in memory.
Follow-up: Write a generator for the Fibonacci sequence.
Real-world: Reading a 100GB log file line-by-line.
Mistake: Using list comprehensions for massive datasets instead of generator expressions.
Decorators.
Concept: Modifying function behavior.
Answer: Functions that take another function as an argument, add functionality, and return a new function.
Follow-up: Write a decorator to measure execution time.
Real-world: Logging, authentication checks, retry logic on API calls.
Mistake: Forgetting @wraps from functools to preserve the original function's metadata.
Multiprocessing vs Multithreading.
Concept: Concurrency vs Parallelism.
Answer: Multithreading is for I/O-bound tasks (network calls) due to the GIL (Global Interpreter Lock). Multiprocessing bypasses the GIL for CPU-bound tasks (heavy math) by using separate memory spaces.
Follow-up: What is the GIL?
Real-world: Multithreading for making concurrent API requests; Multiprocessing for local data transformations.
Mistake: Using multithreading for CPU-heavy tasks, expecting a speedup.
Rapid-Fire Concepts (27):
4. List comprehensions vs Map/Filter.
5. Dictionary internals (Hash tables).
6. Deep copy vs Shallow copy.
7. *args and kwargs.
8. Mutable vs Immutable types.
9. Lambda functions.
10. Exception handling (try/except/finally).
11. Context managers (with statement).
12. Magic/Dunder methods (__init__, __str__).
13. Class methods vs Static methods.
14. Inheritance and Multiple Inheritance (MRO).
15. Set operations (union, intersection).
16. Python memory management and Garbage Collection.
17. is vs ==.
18. Yield from.
19. Asyncio basics.
20. File I/O operations.
21. Pandas: loc vs iloc.
22. Pandas: Handling missing data.
23. Virtual environments.
24. __name__ == "__main__".
25. Time complexity of list/dict operations.
26. Sorting algorithms implementations.
27. String immutability implications.
28. Closures.
29. Type hinting.
30. Unit testing (pytest/unittest).
Top 30 GCP Questions
Detailed Breakdown (Top 3):
Dataproc vs Dataflow.
Concept: Choosing the right compute engine.
Answer: Dataproc is managed Hadoop/Spark (lift-and-shift, highly customizable, good for existing PySpark code). Dataflow is serverless Apache Beam (auto-scaling, unified batch/streaming, no infrastructure management).
Follow-up: Which one scales faster for a sudden spike in streaming data? (Dataflow).
Real-world: Migrating on-prem Spark jobs (Dataproc) vs building a net-new real-time fraud detection pipeline (Dataflow).
Mistake: Suggesting Dataflow just because it's newer, ignoring the cost of rewriting existing PySpark code.
Pub/Sub architecture and delivery guarantees.
Concept: Asynchronous messaging.
Answer: Decoupled publisher/subscriber model. Offers "at-least-once" delivery. Does not guarantee strict ordering natively (unless message ordering is explicitly enabled).
Follow-up: How do you handle duplicate messages in the downstream pipeline?
Real-world: Ingesting global point-of-sale transactions.
Mistake: Assuming exactly-once delivery without implementing idempotency downstream.
BigQuery Partitioning vs Clustering.
Concept: Query optimization in Data Warehousing.
Answer: Partitioning divides a table into segments based on a date/time/integer column (prunes data read). Clustering sorts data based on up to 4 columns (improves filter and join performance).
Follow-up: When would you use clustering over partitioning? (High cardinality columns like customer_id).
Real-world: Querying only yesterday's Amex transactions out of a 10-year history.
Mistake: Partitioning on a column with too many distinct values (limit is 4000 partitions per table).
Rapid-Fire Concepts (27):
4. Cloud Run vs Cloud Functions.
5. IAM Roles (Primitive vs Predefined vs Custom).
6. Service Accounts vs User Accounts.
7. GCS Storage Classes.
8. BigQuery Slot architecture.
9. BigQuery external tables vs native tables.
10. Dataflow Windowing (Fixed, Sliding, Session).
11. Dataflow Watermarks and Triggers.
12. Pub/Sub Dead Letter Queues (DLQ).
13. BigQuery materialized views.
14. Handling PII data (Cloud DLP).
15. Cloud Composer (Airflow) for orchestration.
16. VPCs and Firewall rules basics.
17. BigTable use cases (Time-series, low latency).
18. Spanner vs Cloud SQL.
19. GCS lifecycle policies.
20. Dataproc ephemeral vs long-running clusters.
21. BigQuery cost optimization.
22. Cloud Run concurrency.
23. Cloud Functions cold starts.
24. Pub/Sub push vs pull subscriptions.
25. Apache Beam PCollections.
26. Cross-region data replication.
27. Monitoring pipelines with Cloud Logging/Monitoring.
28. Secret Manager integration.
29. Terraform for GCP infrastructure.
30. Data Catalog / Dataplex for governance.
Top 20 System Design Questions
Detailed Breakdown (Top 2):
Design a near-real-time fraud detection system for credit card transactions.
Concept: Streaming, low-latency lookups.
Answer: Pub/Sub (ingestion) -> Dataflow (stream processing/windowing) -> Bigtable (feature store for low-latency historical lookups) -> ML Model API (Cloud Run) -> Pub/Sub (alerting).
Follow-up: How do you ensure the transaction processes within 50ms?
Real-world: Core Amex use case.
Mistake: Using BigQuery for real-time transaction lookups (too slow).
Design a robust batch pipeline to ingest external payment data files daily.
Concept: Batch, idempotency, error handling.
Answer: GCS (lands file) -> Cloud Function (triggers on file creation) -> Cloud Composer (orchestrates) -> Dataproc (processes/validates data) -> BigQuery (storage).
Follow-up: If the pipeline fails midway, how do you prevent data duplication on restart?
Real-world: Partner integrations.
Mistake: Hardcoding file paths without parameterizing for backfills.
Rapid-Fire Concepts (18):
3. Design a metric dashboard system (millions of events/sec).
4. Data Lake vs Data Warehouse (Medallion architecture).
5. Designing a CDC (Change Data Capture) pipeline.
6. Handling late-arriving data in streaming.
7. Designing for idempotency (Exactly-once semantics).
8. Migrating from on-prem Hadoop to GCP.
9. Global data replication for disaster recovery.
10. Schema evolution strategy.
11. Designing access control for sensitive financial data.
12. Building an automated backfill system.
13. Designing an API rate limiter.
14. Serverless vs Provisioned infrastructure trade-offs.
15. Designing a generic orchestration framework.
16. Cost optimization for large-scale data systems.
17. Ensuring data quality and observability.
18. Handling slowly changing dimensions (SCD Type 2).
19. Designing an AB testing analytics platform.
20. Event sourcing architecture.
Mock Interview Scenarios (Behavioral/Project)
Scenario 1: Tell me about a time your pipeline failed in production.
Answer Strategy: Use the STAR method. Focus on the root cause analysis (e.g., OOM due to unexpected data volume), the immediate fix, and the long-term architectural change (e.g., implementing partitioning or robust retries).
Scenario 2: How did you handle a disagreement on architectural design?
Answer Strategy: Emphasize data-driven decision-making. Explain how you built a quick POC for both approaches, measured latency and cost, and presented the metrics to the team to align on a direction.
American Express PySpark Interview Scenarios
This video walks through a real scenario-based PySpark question asked in an American Express interview, demonstrating the practical coding expectations.
http://googleusercontent.com/youtube_content/0
