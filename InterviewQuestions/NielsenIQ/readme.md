## HR / Behavioral

* [Easy] Walk me through your resume and your current role.
* [Easy] Why do you want to join NielsenIQ, and why the retail analytics space?
* [Easy] What are you looking for in your next data engineering role?
* [Medium] Tell me about a data project that didn't go the way you expected. What surprised you, and how did you handle it? (Common NIQ question)
* [Medium] How do you prioritize tasks when faced with multiple urgent deadlines?
* [Medium] Describe a time you had to learn a new orchestration tool or framework quickly.
* [Medium] How do you handle constructive criticism on your code during pull requests?
* [Medium] Tell me about a time you disagreed with a data scientist or product manager regarding data architecture.
* [Medium] How do you communicate complex technical blockers to non-technical stakeholders?
* [Medium] Describe your experience working in an Agile/Scrum environment.
* [Medium] Describe a scenario where you mentored a junior engineer.
* [Medium] Explain how you would handle a situation where your team missed a critical project deadline.
* [Hard] Imagine your group is getting a project involving skills you don't possess. You cannot swap tasks. How do you handle it? (Common NIQ question)
* **[Hard] Imagine you are a team lead and your friend deleted an important code file, but you have a prior version.**^^ If you submit the prior version, you might avoid immediate detection. How do you handle this? (Common NIQ question)
* [Hard] What is the most challenging bug you have ever resolved in a production environment?
* [Hard] Tell me about a time you had to compromise on system architecture due to strict time constraints.
* [Hard] Describe a time you proactively identified a data bottleneck and fixed it before it broke production.
* [Hard] How would you explain what a p-value is to someone who is not technical? (Common NIQ question)
* [Hard] What is the probability that Amy wins a game by rolling a six first on a fair die, given she rolls first? (Common NIQ question)

## Python

* [Easy] Explain the difference between lists, tuples, and dictionaries.
* **[Easy] Write a function to return all prime numbers up to an integer N. (Common NIQ question)**^^
* [Easy] Write a function to find the first non-repeating character in a string. (Common NIQ question)
* [Easy] How do you handle deep copy vs. shallow copy?
* [Easy] Explain lambda functions and provide an example using `map` or `filter`.
* [Easy] What are `*args` and `kwargs`?
* [Medium] Develop a function `is_subsequence` to check if one string is a subsequence of another. (Common NIQ question)
* **[Medium] Write a function to sort a list of strings in ascending alphabetical order from scratch, returning a new list.**^^ (Common NIQ question)
* [Medium] How do decorators work? Provide a practical use case.
* [Medium] What are generators, and when should you use them over list comprehensions?
* [Medium] How do you manage Python dependencies using Poetry versus `requirements.txt`?
* [Medium] How do you handle exceptions and configure logging in a robust application?
* [Medium] Explain object-oriented programming concepts and how data abstraction is achieved in Python. (Common NIQ question)
* [Medium] What are Python dataclasses and when would you use them?
* [Medium] How do you handle large datasets in Pandas without running out of memory?
* [Hard] Explain the Global Interpreter Lock (GIL) and its impact on multi-threading in data processing.
* [Hard] How does garbage collection and memory management work in Python?
* [Hard] How would you vectorize a slow Pandas `apply` operation for a dataset with millions of rows?
* [Hard] Explain context managers and how to implement a custom `__enter__` and `__exit__`.

## SQL

* [Easy] Explain the difference between INNER JOIN, LEFT JOIN, and CROSS JOIN.
* [Easy] What is the difference between WHERE and HAVING?
* [Easy] Write a query to find the second highest salary in a department.
* [Easy] How do you handle NULL values in aggregation functions?
* [Easy] Explain the difference between UNION and UNION ALL.
* [Easy] Explain ACID properties in relational databases.
* [Medium] Write a query to calculate the moving average of daily sales over the last 7 days. (Common NIQ question)
* [Medium] Write a query to calculate monthly cohort retention rates. (Common NIQ question)
* [Medium] Explain the execution order of a SQL query.
* [Medium] How do Window Functions work? Provide an example using `ROW_NUMBER()`.
* [Medium] Explain the difference between `RANK()`, `DENSE_RANK()`, and `ROW_NUMBER()`.
* [Medium] What is the difference between a clustered and a non-clustered index?
* [Medium] What are CTEs (Common Table Expressions) and how do they differ from temporary tables?
* [Medium] How do you pivot rows into columns in SQL?
* [Medium] Solve a combinatorics problem using SQL joins. (Common NIQ question)
* [Hard] How do you optimize a slow-running query on a table with 50 million retail transactions?
* [Hard] Write a query to find duplicate records in a table and keep only the latest entry based on a timestamp.
* [Hard] Explain partition elimination in large SQL tables.
* [Hard] Write a query to update a large dimension table applying Type 2 SCD (Slowly Changing Dimensions) logic.

## ETL / Data Pipelines

* [Easy] What is the difference between ETL and ELT?
* [Easy] Explain the differences between batch processing and stream processing.
* [Easy] What is a Data Lake architecture compared to a Data Warehouse?
* [Easy] How do you deal with missing or corrupt records during data extraction?
* [Easy] What is the role of a staging layer in a data warehouse?
* [Easy] What factors determine how often an ETL job should run?s
* [Medium] Explain the concept of Slowly Changing Dimensions (SCD Type 1, 2, 3).
* [Medium] Describe your process for backfilling historical data.
* [Medium] How do you enforce data quality and validation within a pipeline?
* [Medium] Describe how you would design an idempotency mechanism in an ETL job.
* [Medium] Explain the Medallion architecture (Bronze, Silver, Gold).
* [Medium] What are the common file formats used in big data pipelines (Parquet, ORC, Avro), and when do you use each?
* [Medium] Describe a pipeline you built that handled unstructured or semi-structured data.
* [Medium] How do you track data lineage across multiple transformations?
* [Medium] Explain how you would implement alerting for data anomalies.
* [Hard] How do you handle late-arriving data in an incremental ETL pipeline?
* [Hard] How do you handle schema evolution in source systems without breaking the pipeline?
* [Hard] How do you monitor ETL pipelines for data drift?
* [Hard] How do you manage Change Data Capture (CDC) from a relational database to a cloud data warehouse?

## Spark / Distributed Systems

* [Easy] Explain the architecture of Apache Spark (Driver, Executors, Cluster Manager).
* [Easy] What is a Resilient Distributed Dataset (RDD)?
* [Easy] What is the difference between transformations and actions in PySpark?
* [Easy] Explain the differences between Spark DataFrames and RDDs.
* [Easy] Explain the concept of lazy evaluation in Spark.
* [Medium] Explain narrow vs. wide dependencies in Spark.
* [Medium] How does Spark handle shuffling, and why is it an expensive operation?
* [Medium] What is the difference between `repartition()` and `coalesce()`?
* [Medium] Explain how broadcasting works in Spark SQL.
* [Medium] What is the difference between Dask and Spark? When would you use Dask over Spark?
* [Medium] How do you write unit tests for Spark applications?
* [Medium] Describe the difference between `cache()` and `persist()` in PySpark.
* [Medium] How do you process nested JSON or Avro files using PySpark?
* **[Medium] Discuss general Databricks and Spark architecture knowledge.**^^ (Common NIQ question)
* [Hard] Describe how to optimize Spark jobs using broadcasting, partitioning, and caching.
* [Hard] How do you handle data skew in PySpark?
* [Hard] How does the Spark Catalyst Optimizer work?
* [Hard] How do you debug Out of Memory (OOM) errors in a Spark executor?
* [Hard] What is Adaptive Query Execution (AQE) in Spark 3.0?
* [Hard] Explain how checkpointing differs from caching in Spark.

## Airflow / Orchestration

* [Easy] What are the core components of Apache Airflow (Scheduler, Webserver, Worker, Metadata DB)?
* [Easy] Explain what a DAG is in Airflow.
* [Easy] What happens when an Airflow task fails? How do you configure retries?
* [Easy] How do you securely manage passwords and API keys in Airflow?
* [Easy] Describe the concept of catchup in Airflow.
* [Medium] What is the difference between Airflow Operators, Sensors, and Hooks?
* [Medium] How do you implement cross-DAG dependencies?
* [Medium] Explain XCom in Airflow and its limitations.
* [Medium] What is the execution date (logical date) in Airflow versus the actual run date?
* [Medium] How do you parameterize an Airflow DAG?
* [Medium] How do you backfill data for a specific date range using Airflow?
* [Medium] How do you trigger an Airflow DAG externally via API?
* [Medium] What is an SLA miss in Airflow, and how do you monitor for it?
* [Hard] Describe how you would write a custom Airflow Operator.
* [Hard] Explain the differences between Airflow and Dagster.
* [Hard] How does Dagster handle data assets compared to Airflow's task-based approach?
* [Hard] Explain the role of the CeleryExecutor or KubernetesExecutor in scaling Airflow.
* [Hard] How do you handle dynamic DAG generation?
* [Hard] How do you mock external dependencies when unit testing Airflow DAGs?

## GCP / Cloud

* [Easy] Explain the difference between Google Cloud Storage (GCS) and BigQuery.
* [Easy] What is Cloud Build, and how do you use it for CI/CD?
* [Easy] Describe how to securely access GCP services using Service Accounts.
* [Easy] Explain Identity and Access Management (IAM) roles in GCP.
* [Easy] How do you schedule a BigQuery script using Cloud Scheduler?
* [Easy] How would you troubleshoot a permission denied error in GCP?
* [Medium] How does BigQuery architecture separate compute and storage?
* [Medium] What are BigQuery partitioned and clustered tables, and when do you use them?
* [Medium] Explain how Google Kubernetes Engine (GKE) is utilized in data engineering.
* [Medium] How do you transfer a 10TB dataset from on-premise to GCS?
* [Medium] What are the differences between BigQuery and a traditional RDBMS?
* [Medium] How do you load data from GCS into BigQuery programmatically using Python?
* [Medium] Explain the use case for Google Cloud Pub/Sub in real-time pipelines.
* [Medium] Describe how you monitor GCP resource utilization and set billing alerts.
* [Medium] Explain materialized views in BigQuery and their advantages over standard views.
* [Hard] How do you optimize BigQuery costs for a large enterprise with daily terabyte queries?
* [Hard] What is the difference between Dataproc and Dataflow?
* [Hard] What is BigQuery Omni?
* [Hard] How do you handle nested and repeated fields in BigQuery during extraction?

## Docker / CI-CD

* [Easy] What is Docker, and why is it used in data engineering?
* [Easy] Explain the difference between a Docker image and a container.
* [Easy] How do you pass environment variables to a Docker container at runtime?
* [Easy] How do you securely handle secrets in a CI/CD pipeline?
* [Medium] Write a sample Dockerfile for a Python application running a PySpark script.
* [Medium] What is Docker Compose, and how is it used for local testing?
* [Medium] What is the difference between `CMD` and `ENTRYPOINT` in a Dockerfile?
* [Medium] Explain the typical CI/CD lifecycle for a data pipeline.
* [Medium] Describe how Cloud Build integrates with Git for continuous integration.
* [Medium] Explain how you use Git branching strategies (like GitFlow) in a data engineering team.
* [Medium] What happens when a CI pipeline fails? How do you rollback to a previous version?
* [Medium] Describe how you run isolated unit tests inside Docker containers.
* [Medium] Explain how to debug a failing container running in a remote GKE environment.
* [Hard] How do you reduce the size of a Docker image for production deployments?
* [Hard] Explain the concept of multi-stage builds in Docker.
* [Hard] How do you automate testing of SQL models in a CI/CD pipeline?
* [Hard] How do you manage infrastructure as code (e.g., Terraform) in a CI/CD workflow?
* [Hard] How do you cache Docker layers to speed up CI/CD builds?

## ML Data Engineering

* [Easy] How do you manage training versus testing data splits in automated pipelines?
* [Easy] What is the difference between batch prediction and real-time prediction?
* [Easy] How do you ensure data privacy (e.g., PII removal) before model training?
* **[Easy] Clean missing data from a Pandas DataFrame meant for ML training.**^^ (Common NIQ question)
* [Medium] What is a feature store, and why is it important for ML models?
* [Medium] How do you handle data versioning for ML datasets?
* [Medium] What tools do you use for tracking model experiments and dataset versions (e.g., DVC, MLflow)?
* [Medium] Explain how to containerize an ML inference script.
* [Medium] Describe how you handle missing values or outliers before feeding data into an ML pipeline.
* [Medium] How do you deploy a trained PyTorch/Scikit-Learn model via an API?
* [Medium] Explain the concept of reproducible ML pipelines.
* [Medium] What format is most efficient for storing large-scale ML datasets?
* [Medium] How do you orchestrate a pipeline that retrains a model weekly using Dagster or Airflow?
* [Hard] Explain the difference between offline and online feature serving.
* [Hard] Describe the workflow of deploying a Jupyter Notebook to a production environment.
* [Hard] How do you optimize a data pipeline specifically for model training (e.g., batching, pre-fetching)?
* [Hard] What is data leakage in machine learning, and how do you prevent it at the pipeline level?
* [Hard] How do you monitor production ML data pipelines for data drift?
* [Hard] How do you scale data preprocessing for deep learning models using PySpark or Dask?
* [Hard] Describe the challenges of deploying ML pipelines in Kubernetes (GKE).

## System Design

* [Easy] Design a robust alerting and monitoring dashboard for an enterprise data platform.
* [Medium] Design a scalable system to scrape, store, and analyze daily pricing from multiple e-commerce sites.
* [Medium] Design a streaming architecture to capture and analyze user clickstream data.
* [Medium] Choose and justify the database technologies for a system handling high read/write volume (e.g., NoSQL vs SQL).
* [Medium] Architect a solution to integrate legacy flat files into a modern BigQuery data warehouse.
* [Medium] Architect a scalable API layer to serve aggregated retail data to external clients.
* [Medium] How do you decouple extraction from transformation logic in a large-scale architecture?
* [Medium] Design a centralized logging system for all microservices and Spark jobs.
* [Medium] Design a system to track inventory changes in real-time across multiple retail chains.
* [Hard] Design a data platform capable of processing 60 billion retail records daily.
* [Hard] How would you architect an end-to-end data pipeline for a real-time recommendation engine?
* [Hard] How would you design a data warehouse architecture for a global FMCG client?
* [Hard] How do you design for high availability and disaster recovery in GCP?
* [Hard] Design an automated model retraining pipeline that handles schema evolution seamlessly.
* [Hard] How do you design a data pipeline to ensure GDPR compliance and right-to-be-forgotten requests?
* [Hard] Design a backfill strategy for 5 years of historical data while production pipelines continue running.
* [Hard] Architect a data cataloging solution to track metadata across BigQuery and GCS.
* [Hard] How would you handle a scenario where data volume grows 10x in a single month?
* [Hard] What architecture would you use to serve ML model predictions within 50ms latency?

## Debugging / Production Scenarios

* [Easy] Scenario: A Docker container runs locally but crashes immediately in the GCP dev environment. What do you check?
* [Easy] Scenario: An upstream data provider changed a column name, breaking the daily ETL job. How do you recover?
* [Easy] Scenario: A merge conflict in Git resulted in a broken DAG pushed to production. How do you quickly resolve and restore service?
* [Medium] Scenario: A PySpark job that normally takes 1 hour is suddenly taking 5 hours. What steps do you take to identify the issue?
* [Medium] Scenario: The BI dashboard is showing incorrect metrics. Walk me through your troubleshooting process from dashboard to source.
* [Medium] Scenario: Duplicate records are discovered in a BigQuery Gold table. How do you find the root cause and fix it?
* [Medium] Scenario: Storage costs in BigQuery spiked by 200% over the weekend. How do you investigate?
* [Medium] Scenario: You are encountering an OOM error in Pandas when processing a single 10GB CSV file on a machine with 8GB RAM. How do you resolve it?
* [Medium] Scenario: A downstream Data Scientist complains the ML pipeline features have missing data for the last 3 days. What is your action plan?
* [Hard] Scenario: Your Airflow DAG failed silently without triggering any alerts or changing the status in the UI. How do you debug?
* [Hard] Scenario: Your API serving ML predictions is throwing intermittent 502 Bad Gateway errors in GKE. How do you debug?
* [Hard] Scenario: Dask workers are continually disconnecting during a large compute job. How do you diagnose the networking or memory issue?
* [Hard] Scenario: A backfill job for last year's data is causing deadlocks in the production SQL database. How do you resolve this without stopping real-time inserts?
* [Hard] Scenario: A new model deployed via Notebook integration is producing predictions with a completely different distribution than in staging. How do you trace the pipeline discrepancy?

[NIQ Interview questions &amp; experience](https://www.youtube.com/watch?v=E9nKNLvCOgI)

This video outlines the overall interview process, assessment formats, and specific behavioral and technical questions candidates face during NielsenIQ recruitment.
