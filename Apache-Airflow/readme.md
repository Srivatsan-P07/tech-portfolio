# Apache-Airflow Course

| **Module**                             | **Topic**                | **Details**                                       |
| -------------------------------------------- | ------------------------------ | ------------------------------------------------------- |
| **1. Introduction to Airflow**         | What is Airflow?               | Use cases, history, and key benefits                    |
|                                              | Architecture Overview          | Components: Scheduler, Web Server, Workers, Metadata DB |
|                                              | Installation & Setup           | Installing via pip, Docker, and Airflow UI overview     |
| **2. Core Concepts**                   | DAGs (Directed Acyclic Graphs) | Structure, scheduling, dependencies                     |
|                                              | Tasks & Operators              | PythonOperator, BashOperator, EmailOperator, etc.       |
|                                              | Task Lifecycle                 | States: success, failed, skipped, etc.                  |
|                                              | Variables, Connections & XComs | Sharing data and configuration between tasks            |
| **3. Developing Workflows**            | Writing Your First DAG         | Simple hello-world DAG                                  |
|                                              | Scheduling DAGs                | Cron expressions,`@daily`,`@hourly`, etc.           |
|                                              | Branching & SubDAGs            | Conditional workflows, best practices                   |
| **4. Advanced Operators & Hooks**      | Common Operators               | PythonOperator, BranchPythonOperator, DummyOperator     |
|                                              | Hooks & Connections            | PostgreSQLHook, MySQLHook, S3Hook, etc.                 |
|                                              | Sensors                        | ExternalTaskSensor, TimeSensor, FileSensor              |
| **5. Integrations**                    | Databases                      | Connecting to MySQL, Postgres, BigQuery                 |
|                                              | Cloud Services                 | AWS (S3, Redshift), GCP (GCS, BigQuery, Pub/Sub), Azure |
|                                              | Data Pipelines                 | Ingest-transform-load pipelines using Pandas/Spark      |
| **6. Airflow in Production**           | Production-grade Setup         | Docker, CeleryExecutor, KubernetesExecutor              |
|                                              | Monitoring & Logging           | Airflow logs, email alerts, SLA miss                    |
|                                              | Scaling                        | Executor types, performance tuning                      |
| **7. Best Practices & Tips**           | Code Organization              | Using templates, separating logic and config            |
|                                              | Version Control                | Using Git with DAGs                                     |
|                                              | Testing DAGs                   | Unit tests with `pytest`, mocking, debugging          |
| **8. Security & Access Control**       | User Management                | Roles, permissions                                      |
|                                              | Authentication                 | LDAP, OAuth, Google Auth                                |
| **9. Airflow Plugins & Extensibility** | Creating Custom Operators      | Build your own operators and sensors                    |
|                                              | Plugin Development             | Adding new views, menu items                            |

.
