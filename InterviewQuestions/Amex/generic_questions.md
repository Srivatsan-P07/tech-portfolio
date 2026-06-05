# Amex Generic Interview Questions

## Top 30 GCP Questions

### 1. Dataproc vs Dataflow.
**Question:** When should you use Dataproc versus Dataflow?
**Answer:** Dataproc is managed Hadoop/Spark for lift-and-shift workloads and PySpark code reuse. Dataflow is serverless Apache Beam for unified batch and streaming with auto-scaling.
**Follow-up:** Dataflow typically scales faster for sudden streaming spikes.
**Mistake:** Choosing Dataflow only because it is newer, without considering rewrite cost.

### 2. Pub/Sub architecture and delivery guarantees.
**Question:** What are Pub/Sub delivery guarantees?
**Answer:** Pub/Sub is asynchronous and offers at-least-once delivery by default. Strict ordering is not guaranteed unless explicitly enabled.
**Follow-up:** Handle duplicates downstream with idempotency.

### 3. BigQuery Partitioning vs Clustering.
**Question:** When should you use partitioning versus clustering in BigQuery?
**Answer:** Partitioning divides data by date/time or integer for pruning; clustering sorts by high-cardinality columns to improve filter and join performance.
**Follow-up:** Use clustering when filtering on high-cardinality columns like `customer_id`.
**Mistake:** Partitioning on too many distinct values, which can exceed partition limits.

### 4. Cloud Run vs Cloud Functions.
**Question:** What is the difference between Cloud Run and Cloud Functions?
**Answer:** Cloud Functions is event-driven serverless functions for simple tasks; Cloud Run deploys containerized services with more control over runtime and concurrency.

### 5. IAM Roles (Primitive vs Predefined vs Custom).
**Question:** How do IAM role types differ?
**Answer:** Primitive roles are broad owner/editor/viewer roles. Predefined roles are service-specific and more granular. Custom roles are user-defined with exact permissions.

### 6. Service Accounts vs User Accounts.
**Question:** When do you use service accounts instead of user accounts?
**Answer:** Service accounts are for automated services and apps; user accounts are for human users.

### 7. GCS Storage Classes.
**Question:** How do GCS storage classes differ?
**Answer:** Coldline and Archive are for long-term storage, Nearline for infrequent access, Standard for hot data.

### 8. BigQuery Slot architecture.
**Question:** What are BigQuery slots?
**Answer:** Slots are units of computational capacity for query execution; more slots can improve concurrency and performance.

### 9. BigQuery external tables vs native tables.
**Question:** When use external tables?
**Answer:** Use external tables when querying data directly from GCS without loading it into BigQuery, trading query speed for storage flexibility.

### 10. Dataflow Windowing (Fixed, Sliding, Session).
**Question:** What are common Dataflow window types?
**Answer:** Fixed windows group events into fixed-size intervals; sliding windows overlap; session windows group events around activity gaps.

### 11. Dataflow Watermarks and Triggers.
**Question:** Why are watermarks and triggers important?
**Answer:** Watermarks represent event-time progress; triggers determine when results are emitted for late or incomplete windows.

### 12. Pub/Sub Dead Letter Queues (DLQ).
**Question:** What is a Pub/Sub DLQ?
**Answer:** A DLQ captures messages that cannot be processed after retries, enabling later inspection and reprocessing.

### 13. BigQuery materialized views.
**Question:** What are materialized views used for?
**Answer:** Materialized views cache query results to speed repeated reads, with trade-offs in refresh cost.

### 14. Handling PII data (Cloud DLP).
**Question:** How do you protect PII in GCP?
**Answer:** Use Cloud DLP to classify, mask, or tokenise sensitive data before storing or analyzing it.

### 15. Cloud Composer (Airflow) for orchestration.
**Question:** When use Cloud Composer?
**Answer:** Use Cloud Composer for managed Apache Airflow orchestration across data workflows.

### 16. VPCs and Firewall rules basics.
**Question:** Why are VPCs and firewall rules important?
**Answer:** They isolate network traffic and control access between services.

### 17. BigTable use cases (Time-series, low latency).
**Question:** When use BigTable?
**Answer:** Use BigTable for large-scale, low-latency time-series or key-value workloads.

### 18. Spanner vs Cloud SQL.
**Question:** When choose Spanner over Cloud SQL?
**Answer:** Use Spanner for globally distributed, strongly consistent relational workloads; Cloud SQL for managed single-region relational databases.

### 19. GCS lifecycle policies.
**Question:** What do lifecycle policies do?
**Answer:** Automate object transitions between storage classes and expiration.

### 20. Dataproc ephemeral vs long-running clusters.
**Question:** How do cluster types differ?
**Answer:** Ephemeral clusters are temporary for on-demand jobs; long-running clusters keep state and can reduce startup cost.

### 21. BigQuery cost optimization.
**Question:** How do you reduce BigQuery costs?
**Answer:** Prune data with partitioning/clustering, avoid `SELECT *`, use cached results, and prefer batched ingestion.

### 22. Cloud Run concurrency.
**Question:** How does concurrency work in Cloud Run?
**Answer:** Cloud Run can handle multiple requests per container instance, reducing cold starts and improving efficiency.

### 23. Cloud Functions cold starts.
**Question:** What causes cold starts?
**Answer:** Cold starts occur when a new function instance is created; keep the runtime warm or use minimal initialization.

### 24. Pub/Sub push vs pull subscriptions.
**Question:** When choose push vs pull?
**Answer:** Push sends messages to an endpoint automatically. Pull lets consumers poll and control processing pace.

### 25. Apache Beam PCollections.
**Question:** What is a PCollection?
**Answer:** A PCollection is Beam's abstraction for a distributed dataset in a pipeline.

### 26. Cross-region data replication.
**Question:** Why replicate data across regions?
**Answer:** For disaster recovery, low latency, and availability.

### 27. Monitoring pipelines with Cloud Logging/Monitoring.
**Question:** How do you monitor pipelines?
**Answer:** Use Cloud Monitoring dashboards, logs, alerts, and tracing for pipeline health and failures.

### 28. Secret Manager integration.
**Question:** How do you handle secrets in GCP?
**Answer:** Store credentials in Secret Manager and fetch them securely from applications.

### 29. Terraform for GCP infrastructure.
**Question:** Why use Terraform?
**Answer:** Terraform provides infrastructure as code for reproducible GCP resource provisioning.

### 30. Data Catalog / Dataplex for governance.
**Question:** What are Data Catalog and Dataplex used for?
**Answer:** They provide metadata management, data discovery, and governance for enterprise datasets.

## Top 20 System Design Questions

### 1. Design a near-real-time fraud detection system for credit card transactions.
**Answer:** Ingest transactions with Pub/Sub, process via Dataflow streaming with windowing, look up historical features in Bigtable, call an ML model API in Cloud Run, and emit alerts through Pub/Sub.
**Follow-up:** Ensure processing within 50ms by using low-latency storage, efficient streaming windows, and autoscaling.
**Mistake:** Using BigQuery for real-time lookups because it is too slow for sub-second response.

### 2. Design a robust batch pipeline to ingest external payment data files daily.
**Answer:** Land files in GCS, trigger Cloud Functions on file creation, orchestrate with Cloud Composer, process/validate in Dataproc, and load results into BigQuery.
**Follow-up:** Prevent duplication on restart with idempotent loads, staging tables, or transactional inserts.
**Mistake:** Hardcoding file paths instead of parameterizing for backfills.

### 3. Design a metric dashboard system (millions of events/sec).
**Answer:** Use event ingestion with Pub/Sub or Kafka, stream aggregation in Dataflow, store metrics in BigQuery or a time-series DB, and visualize in Looker or Grafana.

### 4. Data Lake vs Data Warehouse (Medallion architecture).
**Answer:** Data lakes store raw data cheaply; warehouses store curated analytics data. Medallion architecture layers raw, clean, and curated data.

### 5. Designing a CDC (Change Data Capture) pipeline.
**Answer:** Use source DB change logs, stream them into Pub/Sub or Kafka, transform deltas in Dataflow, and apply them to analytical storage.

### 6. Handling late-arriving data in streaming.
**Answer:** Use event-time windows, watermarks, and allowed lateness to incorporate delayed events.

### 7. Designing for idempotency (Exactly-once semantics).
**Answer:** Add deduplication keys, transactional writes, and idempotent consumers to avoid duplicate processing.

### 8. Migrating from on-prem Hadoop to GCP.
**Answer:** Assess workloads, choose Dataproc or Dataflow, move data to GCS, and adapt pipelines with minimal rewrite.

### 9. Global data replication for disaster recovery.
**Answer:** Replicate data across regions with multi-region storage and cross-region backups.

### 10. Schema evolution strategy.
**Answer:** Use compatible schema changes, versioning, and format features like Avro/Parquet schema evolution.

### 11. Designing access control for sensitive financial data.
**Answer:** Apply least privilege IAM, row-level security, data masking, and audit logging.

### 12. Building an automated backfill system.
**Answer:** Parameterize jobs by date range, checkpoint progress, and support safe re-execution.

### 13. Designing an API rate limiter.
**Answer:** Use token buckets, quotas, or gateway-based throttling with caching.

### 14. Serverless vs Provisioned infrastructure trade-offs.
**Answer:** Serverless offers lower ops and auto-scaling; provisioned gives more control and predictable cost.

### 15. Designing a generic orchestration framework.
**Answer:** Use directed acyclic graphs, parameterized tasks, retries, and observability for workflow pipelines.

### 16. Cost optimization for large-scale data systems.
**Answer:** Right-size resources, use partitioning, delete unused storage, and choose appropriate compute products.

### 17. Ensuring data quality and observability.
**Answer:** Add validation checks, monitoring, alerting, and data quality dashboards.

### 18. Handling slowly changing dimensions (SCD Type 2).
**Answer:** Track historical row versions with effective dates and current flags.

### 19. Designing an AB testing analytics platform.
**Answer:** Capture experiment assignment, funnel events, and compute metrics by cohort in analytics storage.

### 20. Event sourcing architecture.
**Answer:** Store events as the source of truth and derive state through event replay or projections.

## Mock Interview Scenarios (Behavioral / Project)

### Scenario 1: Tell me about a time your pipeline failed in production.
**Answer Strategy:** Use STAR. Describe the situation (e.g., OOM due to unexpected volume), the task, the action taken to fix it, and the result. Highlight root cause analysis and long-term fixes like partitioning or retry logic.

### Scenario 2: How did you handle a disagreement on architectural design?
**Answer Strategy:** Emphasize data-driven decision making. Describe building a quick proof-of-concept for both options, measuring latency and cost, and aligning the team with evidence.
