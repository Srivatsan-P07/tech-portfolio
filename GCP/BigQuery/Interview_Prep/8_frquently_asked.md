* **Window Functions & Time-Series Analysis**
* Calculate a 7-day rolling average for daily sales or sensor readings using `AVG() OVER`.
* Rank the top 3 highest-revenue items per category, managing ties with `DENSE_RANK()`.
* Find the exact duration between consecutive events (e.g., vehicle engine start and stop) using `LEAD()` or `LAG()`.


* **Data Deduplication & Cleansing**
* Remove duplicate records from a massive table while keeping the row with the most recent timestamp using `ROW_NUMBER()`.
* Identify and isolate anomalous data points (e.g., readings 3 standard deviations above the mean).


* **Gaps and Islands Problems**
* Group consecutive dates of activity into a single date range (start_date, end_date) to find continuous user engagement (Islands).
* Identify missing sequential IDs or dates with no logged activity in a time series (Gaps).


* **Hierarchical Data (Highly relevant for automotive like Ford)**
* Traverse a Bill of Materials (BOM) using a Recursive CTE to find all sub-components required for a final assembly.
* Map a complete employee organizational chart from a standard `employee_id` and `manager_id` table.


* **Data Warehousing & ETL Logic**
* Implement Slowly Changing Dimension (SCD) Type 2 logic via SQL (closing out `end_date` on old records and inserting new active rows).
* Compare a source table and a target table to flag rows as 'Insert', 'Update', or 'Delete' (Change Data Capture logic).


* **Performance & Optimization Scenarios**
* Rewrite an inefficient `NOT IN` subquery (handling NULL failures) using `NOT EXISTS` or a `LEFT JOIN ... WHERE NULL`.
* Resolve a slow `JOIN` caused by data skew (e.g., joining on a key where 90% of values are NULL or identical) using key salting.


* **Complex Joins & Pivoting**
* Find overlapping date ranges (e.g., overlapping vehicle rental bookings) using self-joins and date comparison operators.
* Convert row-based key-value telemetry data into a structured columnar format using `PIVOT` or `CASE WHEN` aggregations.