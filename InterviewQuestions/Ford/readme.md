# Ford Interview Questions

## SQL

1. Find the 3rd highest salary per department without using `DENSE_RANK()`.
2. Identify overlapping date ranges in a subscription or session table.
3. Calculate a 7-day rolling average of vehicle sensor readings.
4. Optimize a query performing a full table scan on a 50B row BigQuery table.
5. Use window functions to find the time difference between consecutive events for a single vehicle ID.
6. Handle skewed joins in BigQuery.
7. Pivot rows into columns dynamically.
8. Explain the difference between `PARTITION BY` and `GROUP BY` with an execution example.
9. Resolve a "Resources Exceeded" error in BigQuery.
10. Find missing sequence gaps in a time-series telemetry table.

## Python

11. Flatten a deeply nested JSON payload from a REST API.
12. Explain how the Global Interpreter Lock (GIL) impacts Python data processing.
13. Write a generator function to process a 100GB CSV file line by line without OOM errors.
14. Detect and handle memory leaks in a long-running Python process.
15. Implement a caching decorator to optimize repetitive database calls.
16. Deduplicate records in a list of dictionaries based on two composite keys.
17. Compare `multiprocessing` vs `asyncio` for I/O-bound API extraction.

## Dataflow & Apache Beam Optimization

18. Handle side inputs in Apache Beam when side input data updates dynamically during a streaming pipeline.
19. Explain the architectural difference between `GroupByKey` and `Combine` and their impact on shuffle data size.
20. Diagnose a pipeline suffering from high system lag or stuck steps using Dataflow monitoring metrics.
21. Compare operational differences and resource impacts of tumbling versus sliding windows for vehicle speed aggregations.
22. Mitigate key distribution skew (hot keys) under Dataflow’s streaming auto-scaling.
23. Apply `ValueState` and `BagState` for an automotive use case requiring stateful processing.
24. Maintain exactly-once processing when consuming from Pub/Sub and writing to an external downstream database.

## Data Modeling

25. Design a data model for an automotive IoT telemetry system.
26. Compare star schema vs snowflake schema and identify when star is inferior.
27. Handle Slowly Changing Dimensions (SCD) Type 2 for shifting dealership locations.
28. Design a schema supporting both real-time operational analytics and historical ML training.
29. Define a data mesh and structure potential data domains for Ford.
30. Model hierarchical data for car part assemblies (BOM).

## System Design

31. Architect an end-to-end pipeline ingesting 1M telemetry events per second.
32. Design an idempotent ETL pipeline.
33. Sync an on-premise Oracle database to BigQuery with minimal latency.
34. Design a scalable alerting system for vehicle diagnostic anomalies.
35. Ensure data quality and lineage across a multi-stage GCP pipeline.
36. Justify choices between batch, micro-batch, and streaming for different business use cases.

## Cloud Architecture (GCP & Ford Stack)

37. Explain BigQuery's separation of compute and storage.
38. Compare Cloud Dataflow (Apache Beam) vs Dataproc (Spark) use cases.
39. Optimize BigQuery computing costs for a BI team running heavy exploratory queries.
40. Detail the role of Terraform in deploying cloud data infrastructure.
41. Secure secrets and environment variables in Airflow (Cloud Composer).
42. Outline a CI/CD workflow using Tekton and Artifact Registry.
43. Integrate dbt or Dataform with BigQuery for analytics engineering.

## Production Debugging / Incident Handling

44. Detail investigation steps for a daily Airflow DAG that failed silently.
45. Troubleshoot and resolve a severely lagging Kafka consumer.
46. Execute incident response for downstream data validation check failures.
47. Backfill 6 months of historical data without violating active production SLAs.

## Behavioral

48. Describe a technical decision you made that successfully reduced tech debt.
49. Detail your approach to convincing stubborn stakeholders to adopt a new framework.
50. Explain a scenario where you missed a critical deadline and your mitigation strategy.
