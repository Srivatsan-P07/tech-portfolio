**Input Sample Dataset**

```sql
WITH user_activity AS (
  SELECT 101 AS user_id, DATE '2026-03-01' AS activity_date UNION ALL
  SELECT 101, DATE '2026-03-02' UNION ALL
  SELECT 101, DATE '2026-03-03' UNION ALL
  SELECT 101, DATE '2026-03-06' UNION ALL
  SELECT 101, DATE '2026-03-07' UNION ALL
  SELECT 102, DATE '2026-03-01' UNION ALL
  SELECT 102, DATE '2026-03-05'
)

```

---

**1. Interval Arithmetic**

Adds or subtracts temporal units from a date or timestamp.

* `DATE_ADD(date_expr, INTERVAL n PART)`: Moves date forward.
* `DATE_SUB(date_expr, INTERVAL n PART)`: Moves date backward.
* Standard syntax uses `INTERVAL n UNIT` (e.g., `DAY`, `MONTH`, `YEAR`, `WEEK`).

```sql
SELECT
  user_id,
  activity_date,
  DATE_ADD(activity_date, INTERVAL 7 DAY)   AS next_week,
  DATE_SUB(activity_date, INTERVAL 1 MONTH) AS last_month
FROM user_activity;

```

---

**2. Difference, Truncation & Extraction**

* **`DATE_DIFF(end_date, start_date, UNIT)`**: BigQuery uses `DATE_DIFF(a, b, UNIT)` computing $a - b$ (Standard SQL).
* **`DATE_TRUNC(date_expr, UNIT)`**: Resets date to the first day of that period (week, month, quarter, year).
* **`EXTRACT(PART FROM date_expr)`**: Pulls specific numeric component (day of week, year, month). Note: BigQuery does not use `DATEPART()`; `EXTRACT()` is the ANSI/BigQuery standard.

```sql
SELECT
  activity_date,
  -- Difference between activity date and fixed baseline
  DATE_DIFF(activity_date, DATE '2026-03-01', DAY) AS days_since_start,
  -- Truncate to start of month
  DATE_TRUNC(activity_date, MONTH) AS month_start,
  -- Extract specific parts
  EXTRACT(DAYOFWEEK FROM activity_date) AS day_of_week, -- 1 = Sunday, 7 = Saturday
  EXTRACT(YEAR FROM activity_date)      AS activity_year
FROM user_activity;

```

---

**3. Gaps & Islands**

Used to identify continuous streaks ("islands") or missing intervals ("gaps").

**Islands (Finding Consecutive Streaks)**

* *Core Logic*: Subtracting a sequence `ROW_NUMBER()` from the date produces an identical anchor date for uninterrupted streaks.

```sql
WITH numbered_activity AS (
  SELECT
    user_id,
    activity_date,
    -- Subtract row number (in days) from the activity date
    DATE_SUB(activity_date, INTERVAL ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY activity_date) DAY) AS streak_group
  FROM user_activity
)
SELECT
  user_id,
  MIN(activity_date) AS streak_start_date,
  MAX(activity_date) AS streak_end_date,
  COUNT(*)           AS streak_length_days
FROM numbered_activity
GROUP BY user_id, streak_group
ORDER BY user_id, streak_start_date;

```

**Gaps (Finding Missing Date Intervals)**

* *Core Logic*: Use `LAG()` or `LEAD()` to compare adjacent rows. A `DATE_DIFF() > 1` signals a gap.

```sql
WITH date_lags AS (
  SELECT
    user_id,
    activity_date,
    LAG(activity_date) OVER (PARTITION BY user_id ORDER BY activity_date) AS prev_date
  FROM user_activity
)
SELECT
  user_id,
  DATE_ADD(prev_date, INTERVAL 1 DAY)     AS gap_start_date,
  DATE_SUB(activity_date, INTERVAL 1 DAY)  AS gap_end_date,
  DATE_DIFF(activity_date, prev_date, DAY) - 1 AS missing_days_count
FROM date_lags
WHERE DATE_DIFF(activity_date, prev_date, DAY) > 1;

```

---

**Key Differences & Interview Traps**

| Function / Concept | Syntax Rule (BigQuery) | Interview Note |
| --- | --- | --- |
| **`DATE_DIFF`** | `DATE_DIFF(end, start, UNIT)` | Argument order matters: `end - start`. Positive if `end > start`. |
| **`EXTRACT` vs `DATEPART**` | `EXTRACT(PART FROM date)` | BigQuery uses `EXTRACT()`, not T-SQL's `DATEPART()`. |
| **`DATE_TRUNC`** | `DATE_TRUNC(date, MONTH)` | Returns a `DATE` type normalized to the period start. |
| **Islands Method** | `date - ROW_NUMBER()` | Preserves a constant `DATE` grouping key across consecutive days. |
| **Gaps Method** | `LAG()` / `LEAD()` + `DATE_DIFF` | Identifies where difference between sequential rows exceeds threshold. |