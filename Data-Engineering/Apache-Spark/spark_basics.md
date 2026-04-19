| Topic | Description | Importance | Example Task |
| :--- | :--- | :--- | :--- |
| **DataFrames Basics** | Creating DataFrames, schema, reading data (CSV, JSON) | Most-used API in PySpark | Load a CSV and print schema + show data |
| **DataFrame Operations** | select, filter, withColumn, drop | Core transformations | Filter rows, create new columns |
| **Column Expressions** | Using functions like col, lit, when | Writing logic in Spark-friendly way | Create conditional columns |
| **Aggregations** | groupBy, agg, count, sum, avg | Used in analytics and reporting | Group sales data by category |
| **Joins** | Inner, left, right joins | Combine datasets | Join two datasets (users + orders) |
| **Spark SQL** | Writing SQL queries using Spark SQL | Easier for SQL users | Register temp view and query using SQL |
| **Built-in Functions** | String, date, math functions | Avoids Python loops (important!) | Parse dates, clean strings |
| **Handling Missing Data** | dropna, fillna | Real-world data is messy | Replace null values with defaults |
| **RDD Basics (Optional)** | What RDDs are, basic transformations | Helps understand Spark internals | Convert DataFrame to RDD and back |
| **Performance Basics** | Lazy evaluation, transformations vs actions, caching | Prevent slow jobs | Use .cache() and compare execution times |
| **Partitioning** | Repartition vs coalesce | Controls performance and parallelism | Experiment with partitions and file sizes |
| **File Formats** | Parquet vs CSV | Efficient storage matters | Save data as Parquet and compare speed |