# Amex SQL Interview Questions

## Top 5 Detailed SQL Questions

### 1. Find the running total of transactions per customer.
**Answer:** Use a window function with `SUM() OVER(PARTITION BY cust_id ORDER BY txn_date)`.
```sql
SELECT cust_id,
       txn_date,
       amount,
       SUM(amount) OVER (PARTITION BY cust_id ORDER BY txn_date) AS running_total
FROM transactions;
```
**Follow-up:** Performance changes if the `ORDER BY` is removed because the window becomes a partition total instead of a running total.
**Mistake:** Forgetting `ORDER BY` inside `OVER()` returns the same cumulative sum for every row.

### 2. Find the 3rd highest salary in each department.
**Answer:** Use `DENSE_RANK()` over each department and filter where rank = 3.
```sql
WITH ranked_salaries AS (
  SELECT dept_id,
         emp_id,
         salary,
         DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS salary_rank
  FROM employees
)
SELECT dept_id, emp_id, salary
FROM ranked_salaries
WHERE salary_rank = 3;
```
**Follow-up:** `RANK()` can skip numbers on ties, while `DENSE_RANK()` does not.
**Mistake:** Using `product = 'A' AND product = 'B'` instead of aggregation logic.

### 3. Identify gaps in sequential data (e.g., missing transaction IDs).
**Answer:** Compare current ID to `LAG(id)` and flag differences greater than 1.
```sql
SELECT id,
       LAG(id) OVER (ORDER BY id) AS prev_id,
       id - LAG(id) OVER (ORDER BY id) AS gap
FROM transactions
HAVING gap > 1;
```
**Follow-up:** Generate actual missing numbers using a numbers table or recursive CTE.
**Mistake:** Not handling the first row where `LAG()` returns `NULL`.

### 4. Find customers who bought both Product A and Product B.
**Answer:** Use conditional aggregation with `HAVING COUNT(DISTINCT product) = 2`.
```sql
SELECT cust_id
FROM sales
WHERE product IN ('A', 'B')
GROUP BY cust_id
HAVING COUNT(DISTINCT product) = 2;
```
**Follow-up:** Scale to 50 specific products by comparing against a product list and ensuring all required values are present.
**Mistake:** Using `WHERE product = 'A' AND product = 'B'`, which returns no rows.

### 5. Calculate year-over-year growth per month.
**Answer:** Aggregate revenue by month/year and use `LAG()` to compare with the same period last year.
```sql
WITH monthly_revenue AS (
  SELECT DATE_TRUNC('month', txn_date) AS month_year,
         SUM(revenue) AS revenue
  FROM sales
  GROUP BY DATE_TRUNC('month', txn_date)
)
SELECT month_year,
       revenue,
       LAG(revenue, 12) OVER (ORDER BY month_year) AS prior_year_revenue,
       CASE WHEN LAG(revenue, 12) OVER (ORDER BY month_year) = 0 THEN NULL
            ELSE (revenue - LAG(revenue, 12) OVER (ORDER BY month_year)) * 100.0 / LAG(revenue, 12) OVER (ORDER BY month_year)
       END AS yoy_growth_pct
FROM monthly_revenue;
```
**Follow-up:** Handle zero revenue months to avoid division by zero.
**Mistake:** Joining the table to itself instead of using cleaner window functions.

## Rapid-Fire SQL Questions with Answers

6. Recursive CTE for organizational hierarchy.
**Answer:** Use `WITH RECURSIVE` to start from root nodes and union all child rows.

7. Pivot rows to columns without `PIVOT` function.
**Answer:** Use `MAX(CASE WHEN ... THEN ... END)` or conditional aggregation.

8. Unpivot columns to rows.
**Answer:** Use `UNION ALL` of each column or `CROSS APPLY / UNPIVOT` if available.

9. Delete duplicate rows keeping the lowest ID.
**Answer:** Use `ROW_NUMBER() OVER (PARTITION BY cols ORDER BY id)` and delete where row number > 1.

10. Moving average over 7 days.
**Answer:** Use `AVG(value) OVER (ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)`.

11. First and last transaction per customer.
**Answer:** Use `ROW_NUMBER()` or `FIRST_VALUE()` / `LAST_VALUE()` over partition by customer.

12. Customers who churned (no activity in 30 days).
**Answer:** Use `MAX(txn_date)` per customer and compare to current date or use windowed gaps.

13. Finding overlapping date ranges.
**Answer:** Two ranges overlap if `start1 <= end2 AND start2 <= end1`.

14. Cumulative distribution of sales.
**Answer:** Use `CUME_DIST() OVER (ORDER BY sales)`.

15. Median salary calculation.
**Answer:** Use `PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary)` or `ROW_NUMBER()` logic.

16. Join vs Union performance.
**Answer:** Joins combine columns from related rows; unions append rows and may require deduplication with `UNION DISTINCT`.

17. Cross join use cases.
**Answer:** Use when every row in one table must pair with every row in another, such as generating combinations.

18. Handling `NULL`s in `NOT IN` vs `NOT EXISTS`.
**Answer:** `NOT IN` can fail if the subquery contains `NULL`; `NOT EXISTS` is safer for excluding rows.

19. Optimizing queries with indexes.
**Answer:** Add indexes on filter and join columns, avoid full table scans, and use composite indexes for common multi-column filters.

20. Explain plans and execution paths.
**Answer:** Use `EXPLAIN` to check join order, index usage, and estimated row counts; adjust indexes and query structure accordingly.

21. Temporary tables vs CTEs.
**Answer:** CTEs are inline query expressions; temp tables persist for the session and can be indexed or reused.

22. Extracting JSON values in SQL.
**Answer:** Use JSON extraction functions like `JSON_EXTRACT`, `JSON_VALUE`, or `->>` depending on your RDBMS.

23. Percentile calculations.
**Answer:** Use `PERCENTILE_CONT()` or `PERCENTILE_DISC()` window functions.

24. Identifying consecutive streaks.
**Answer:** Use row numbering and `date - row_number()` grouping or window functions to detect sequential values.

25. Rollup vs Cube.
**Answer:** `ROLLUP` aggregates along a hierarchy; `CUBE` computes all combinations of grouping columns.

26. Updating a table based on a join.
**Answer:** Use `UPDATE ... FROM ... JOIN ...` or a merge statement to update target rows from source values.

27. Handling time zones.
**Answer:** Store timestamps in UTC, convert to local zones on presentation, and use timezone-aware types when available.

28. `COALESCE` vs `ISNULL`.
**Answer:** `COALESCE` is standard SQL and accepts multiple arguments; `ISNULL` is vendor-specific and usually accepts two.

29. Exact vs Approximate distinct counts.
**Answer:** Exact counts use `COUNT(DISTINCT ...)`; approximate counts use functions like `APPROX_COUNT_DISTINCT` for large datasets.

30. Finding the most frequent value (Mode).
**Answer:** Use `GROUP BY value ORDER BY COUNT(*) DESC LIMIT 1`.

31. String manipulation (`SUBSTRING`, `REGEXP`).
**Answer:** Use string functions supported by the DB to slice, replace, and search text.

32. Date math (Days between dates).
**Answer:** Use `DATEDIFF()` or date subtraction depending on the database.

33. Materialized views trade-offs.
**Answer:** They improve read performance for expensive queries but require refresh and storage overhead.

34. Partitioning by date.
**Answer:** Use date partitions to prune old data and speed up date-range queries.

35. Clustered vs Non-clustered indexes.
**Answer:** Clustered index defines row order; non-clustered index maintains a separate structure for lookups.

36. Left Anti Join logic.
**Answer:** Return rows in the left table with no matching rows in the right table; can be expressed with `LEFT JOIN ... WHERE right.key IS NULL`.

37. Grouping Sets.
**Answer:** Use `GROUPING SETS` to compute multiple aggregations in a single query.

38. Returning rows with maximum value per group without window functions.
**Answer:** Use a correlated subquery or join against an aggregated result with `MAX()`.

39. Full outer join scenarios.
**Answer:** Use when you need rows present in either table, including unmatched rows from both sides.

40. Case statements for categorical binning.
**Answer:** Use `CASE WHEN ... THEN ... END` to bucket values into categories.

41. Calculating retention rate.
**Answer:** Count users active in both baseline and comparison periods and divide by baseline user count.

42. Sequence generation.
**Answer:** Use a numbers table, recursive CTE, or built-in sequence generator.

43. Upsert (`MERGE`) statements.
**Answer:** Use `MERGE` or `INSERT ... ON CONFLICT/ON DUPLICATE KEY UPDATE` to insert new rows or update existing ones.

44. Handling division by zero safely.
**Answer:** Use `NULLIF(divisor, 0)` or a `CASE WHEN divisor = 0 THEN NULL ELSE numerator/divisor END`.

45. Comparing table schemas.
**Answer:** Query system catalog tables or use `INFORMATION_SCHEMA.COLUMNS` to compare column names, types, and nullability.

46. Finding orphaned records.
**Answer:** Use `LEFT JOIN` with `WHERE right.key IS NULL` to detect parent records without children.

47. Querying hierarchical data without CTEs.
**Answer:** Use adjacency lists with recursive joins, self-joins, or SQL hierarchy functions if available.

48. Triggers and stored procedures (concept).
**Answer:** Triggers execute on table events; stored procedures encapsulate reusable logic with parameters.

49. Row-level security basics.
**Answer:** Enforce data access rules per row using policies or filters based on `CURRENT_USER` or tenant IDs.

50. SQL injection prevention.
**Answer:** Use parameterized queries, bind variables, and never concatenate user input directly into SQL.
