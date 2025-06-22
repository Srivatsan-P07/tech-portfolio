# 📘 **BigQuery Deep-Dive Course (Updated for SQL Users)**

| **Module**                       | **Topic**                              | **Learning Objectives**                                        | **Resources/Practices**              |
| -------------------------------- | -------------------------------------- | -------------------------------------------------------------- | ------------------------------------ |
| **1. Introduction**              | What is BigQuery?                      | Understand purpose, use cases, serverless model.               | Google Cloud Docs, Quickstarts       |
|                                  | Concepts: Datasets, Tables, Projects   | Navigate the workspace.                                        | Hands-on: Setup & Explore            |
|                                  | Differences vs RDBMS                   | Understand what sets BigQuery apart.                           | Compare SQL to BQ behavior           |
| **2. Architecture Deep Dive**    | Dremel Engine                          | Learn how SQL is executed at scale.                            | Read Dremel paper                    |
|                                  | Columnar Storage & Capacitor           | Understand compressed, column-based layout.                    | Analyze storage stats                |
|                                  | Compute-Storage Separation             | Grasp scale-out query execution.                               | Draw architecture diagrams           |
|                                  | Slots, Reservations, and Autoscaling   | Learn about parallelism and concurrency.                       | Monitor slot usage                   |
|                                  | Multi-Tenant Design                    | Understand isolation and SLAs.                                 | GCP articles                         |
| **3. Nested & Complex Data** ✅   | STRUCTs & ARRAYS                       | Learn how BigQuery handles nested schemas.                     | Define nested schemas                |
|                                  | UNNEST() Function                      | Flatten data for analysis.                                     | Practice querying nested JSON        |
|                                  | Working with JSON                      | Use JSON functions in SQL.                                     | Parse and extract JSON fields        |
|                                  | Querying Repeated Records              | Aggregate and filter repeated fields.                          | Build queries on public datasets     |
|                                  | Designing with Nested Data             | Optimize for performance with denormalized but queryable data. | Restructure traditional schemas      |
| **4. Storage & Modeling**        | Native vs External Tables              | Understand table types and their tradeoffs.                    | Practice on GCS & BQ-native tables   |
|                                  | Partitioning (Ingestion, Column, Time) | Control costs & boost speed.                                   | Use partition filters                |
|                                  | Clustering                             | Enable selective scanning.                                     | Tune clustering fields               |
|                                  | Materialized Views                     | Automate freshness with cost savings.                          | Create and compare to standard views |
|                                  | Sharding Patterns (Anti-Pattern)       | Understand why not to use sharded tables.                      | Convert shards to partitions         |
| **5. Query Engine**              | Query Lifecycle & EXPLAIN              | Follow a query through stages.                                 | Analyze query plans                  |
|                                  | Slots and Query Execution Graph        | Visualize how work is distributed.                             | Use Query Plan visualizer            |
|                                  | Query Caching                          | Save costs with automatic caching.                             | Re-run and compare timings           |
|                                  | Query Optimization Techniques          | Optimize joins, filters, subqueries.                           | Benchmark improvements               |
| **6. Performance Engineering**   | Best Practices for Joins, Filters      | Avoid common slow-query traps.                                 | Rewrite slow queries                 |
|                                  | Dry Run & Cost Estimation              | Pre-evaluate cost & slot usage.                                | Enable dry run in console            |
|                                  | Denormalization Strategy               | Adjust SQL assumptions for BigQuery’s scale.                   | Normalize → Denormalize exercise     |
|                                  | Managing Long-Running Queries          | Break into stages or materialize steps.                        | Materialize subqueries               |
| **7. Advanced Features**         | User-Defined Functions (UDFs)          | Write custom logic in SQL & JS.                                | Create and reuse UDFs                |
|                                  | BigQuery ML                            | Train models in SQL: linear, logistic, k-means.                | Model GitHub data                    |
|                                  | BigQuery GIS                           | Geospatial SQL analytics.                                      | Map geodata in Geo Viz               |
|                                  | BigLake & Open Table Formats           | Work with Iceberg, Parquet, Delta Lake.                        | Query GCS with BQ syntax             |
|                                  | Remote Functions                       | Extend SQL with API calls.                                     | Integrate with Cloud Functions       |
| **8. Integration & Ingestion**   | Batch Loads, Streaming Inserts         | Compare load methods and costs.                                | Use bq CLI and Pub/Sub               |
|                                  | Federated Queries                      | Query data in Cloud SQL, GCS, Sheets.                          | Build cross-source queries           |
|                                  | Data Transfer Service                  | Automate SaaS source ingestion.                                | GA → BigQuery integration            |
|                                  | JSON & Semi-Structured Data Pipelines  | Process nested, schema-free data.                              | Ingest and parse JSON                |
| **9. Security & Compliance**     | IAM Roles & Dataset Policies           | Secure access at all levels.                                   | Assign viewer, editor roles          |
|                                  | Column- and Row-Level Security         | Implement fine-grained access controls.                        | Use policy tags & filters            |
|                                  | Audit Logging                          | Track usage and anomalies.                                     | Query audit logs                     |
|                                  | Encryption, Regionality & Sovereignty  | Know where/how data is protected.                              | Explore multi-region setups          |
| **10. Observability & Metadata** | INFORMATION\_SCHEMA Views              | Access table/query/job metadata.                               | Monitor data access patterns         |
|                                  | BI Engine & Caching                    | Optimize BI tools (Looker, Data Studio).                       | Benchmark report performance         |
|                                  | Query & Job Monitoring                 | Track slow or expensive queries.                               | Use Cloud Monitoring dashboards      |
|                                  | Quotas, Limits, Error Messages         | Learn how to debug failed jobs.                                | Catalog common errors                |
| **11. CI/CD & Ops**              | Scheduled Queries                      | Automate workflows & reporting.                                | Build parameterized reports          |
|                                  | dbt + BigQuery                         | Data modeling as code.                                         | Set up dbt project                   |
|                                  | Infrastructure as Code (Terraform)     | Automate dataset/table setup.                                  | Deploy with Terraform                |
|                                  | Unit Testing & Data Contracts          | Enforce schema & quality expectations.                         | Use tools like Great Expectations    |
| **12. Real-World Projects**      | Data Lakehouse on BigQuery + GCS       | Implement end-to-end solution.                                 | Load, transform, analyze             |
|                                  | Streaming Dashboard with Pub/Sub       | Real-time ingestion → visualization.                           | Connect to Data Studio               |
|                                  | E-commerce Analytics                   | Session, conversion, funnel tracking.                          | Model real-world KPIs                |
|                                  | Compliance Audit Report Generation     | Automate security audits.                                      | Build query templates                |

---