**Input Sample Dataset**

```sql
WITH sales_data AS (
  SELECT 'US' AS country, 'Electronics' AS category, 'completed' AS status, 150 AS amount UNION ALL
  SELECT 'US', 'Electronics', 'cancelled', 100 UNION ALL
  SELECT 'US', 'Furniture',   'completed', 300 UNION ALL
  SELECT 'UK', 'Electronics', 'completed', 200 UNION ALL
  SELECT 'UK', 'Furniture',   'completed', 400 UNION ALL
  SELECT 'UK', 'Furniture',   'cancelled', 150
)

```

---

**1. Conditional Aggregation**

Pivots rows into aggregated columns based on conditions without filtering out the underlying dataset.

* `COUNT(CASE WHEN ... THEN 1 END)` counts only non-null values matching the condition.
* `SUM(CASE WHEN ... THEN amount ELSE 0 END)` aggregates specific values while defaulting unmatched rows to `0`.

```sql
SELECT 
  country,
  COUNT(CASE WHEN status = 'completed' THEN 1 END) AS completed_orders_count,
  SUM(CASE WHEN status = 'completed' THEN amount ELSE 0 END) AS completed_sales_sum,
  SUM(CASE WHEN status = 'cancelled' THEN amount ELSE 0 END) AS lost_revenue_sum
FROM sales_data
GROUP BY country;

```

---

**2. Subtotals & Multidimensional Grouping**

BigQuery supports multidimensional aggregations to produce subtotals and grand totals in a single query pass.

* **`GROUPING SETS`**: Computes aggregations strictly for the specified dimension combinations.
* **`ROLLUP`**: Creates hierarchical subtotals from left to right, plus a grand total (e.g., `(A, B)`, `(A)`, `()`).
* **`CUBE`**: Computes all possible permutations of the dimensions ($2^N$ combinations), plus a grand total.

```sql
-- GROUPING SETS: Specific combinations only
SELECT country, category, SUM(amount) AS total_sales
FROM sales_data
GROUP BY GROUPING SETS ((country, category), (country), ())
ORDER BY country NULLS LAST, category NULLS LAST;

-- ROLLUP: Hierarchical subtotals (Country+Category -> Country -> Grand Total)
SELECT country, category, SUM(amount) AS total_sales
FROM sales_data
GROUP BY ROLLUP (country, category)
ORDER BY country NULLS LAST, category NULLS LAST;

-- CUBE: All combinations (Both, Country only, Category only, Grand Total)
SELECT country, category, SUM(amount) AS total_sales
FROM sales_data
GROUP BY CUBE (country, category)
ORDER BY country NULLS LAST, category NULLS LAST;

```

---

**3. Filtering Aggregates: `WHERE` vs `HAVING**`

* **`WHERE`**: Filters **raw rows before** aggregation occurs. Cannot reference aggregate functions like `SUM()` or `COUNT()`.
* **`HAVING`**: Filters **grouped rows after** aggregation occurs. Operates on aggregated values.

```sql
SELECT 
  country,
  category,
  SUM(amount) AS total_completed_sales
FROM sales_data
WHERE status = 'completed'      -- Step 1: Filter raw rows before grouping
GROUP BY country, category
HAVING SUM(amount) > 200;       -- Step 2: Filter aggregated buckets

```

---

**Key Differences Summary**

| Clause / Feature | Execution Point | Primary Use Case |
| --- | --- | --- |
| **Conditional Aggregation** | During aggregation step | Pivot row conditions into metric columns |
| **`ROLLUP`** | Aggregation phase | Hierarchical summaries & grand totals |
| **`CUBE`** | Aggregation phase | Cross-dimensional reporting (all combos) |
| **`GROUPING SETS`** | Aggregation phase | Custom subtotal combinations |
| **`WHERE`** | Pre-aggregation | Row-level data filtering |
| **`HAVING`** | Post-aggregation | Metric-level threshold filtering |