**Input Sample Dataset**

```sql
WITH employees AS (
  SELECT 1 AS emp_id, 'Alice' AS name, 10 AS dept_id, 90000 AS salary, NULL AS manager_id UNION ALL
  SELECT 2,           'Bob',   10,          70000,           1                UNION ALL
  SELECT 3,           'Charlie',20,         80000,           1                UNION ALL
  SELECT 4,           'David', 99,          60000,           2
),
departments AS (
  SELECT 10 AS dept_id, 'Engineering' AS dept_name UNION ALL
  SELECT 20,           'Marketing'               UNION ALL
  SELECT 30,           'Finance'
),
current_year_promotions AS (
  SELECT 1 AS emp_id UNION ALL
  SELECT 2
),
prior_year_promotions AS (
  SELECT 2 AS emp_id UNION ALL
  SELECT 3
)

```

---

**1. Join Types**

* **`CROSS JOIN`**: Cartesian product ($M \times N$ rows). Commonly used for generating date matrices or dimension permutations.
* **`SELF JOIN`**: Joining a table to itself using distinct aliases. Ideal for hierarchies (manager-employee) or comparing adjacent rows.
* **`FULL OUTER JOIN`**: Returns all rows from both tables, populating `NULL` on either side where keys do not match.

```sql
-- CROSS JOIN: Generates all employee-department combinations
SELECT e.name, d.dept_name
FROM employees e
CROSS JOIN departments d;

-- SELF JOIN: Resolves employee-to-manager hierarchy
SELECT 
  e.name AS employee_name,
  m.name AS manager_name
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.emp_id;

-- FULL OUTER JOIN: Retains unassigned employees (David) and empty departments (Finance)
SELECT e.name, d.dept_name
FROM employees e
FULL OUTER JOIN departments d ON e.dept_id = d.dept_id;

```

---

**2. Conditional Joining (`ON` vs `WHERE` on a `LEFT JOIN`)**

* **Condition in `ON**`: Filters the **right** table *before* joining. All left rows are preserved; non-matching right columns become `NULL`.
* **Condition in `WHERE**`: Filters the **result set** *after* joining. Turns a `LEFT JOIN` into an unintentional `INNER JOIN` if referencing right table columns without `IS NULL`.

```sql
-- Filter in ON: Keeps all employees; dept_name is NULL if dept_id != 10
SELECT e.name, d.dept_name
FROM employees e
LEFT JOIN departments d 
  ON e.dept_id = d.dept_id 
  AND d.dept_id = 10;

-- Filter in WHERE: Discards employees not matching the condition (removes Alice/Charlie/David)
SELECT e.name, d.dept_name
FROM employees e
LEFT JOIN departments d 
  ON e.dept_id = d.dept_id
WHERE d.dept_id = 10;

```

---

**3. Set Operations**

Combines distinct result sets vertically. Both queries must share identical column counts and compatible data types.

* **`UNION ALL`**: Appends all rows including duplicates (fastest, no deduplication step).
* **`UNION DISTINCT` (or `UNION`)**: Appends rows and removes exact duplicates.
* **`INTERSECT DISTINCT`**: Returns only rows present in **both** sets.
* **`EXCEPT DISTINCT`**: Returns rows from the first query that **do not exist** in the second (BigQuery standard for `MINUS`).

```sql
-- UNION vs UNION ALL
SELECT emp_id FROM current_year_promotions
UNION DISTINCT
SELECT emp_id FROM prior_year_promotions;  -- Returns: 1, 2, 3

SELECT emp_id FROM current_year_promotions
UNION ALL
SELECT emp_id FROM prior_year_promotions;  -- Returns: 1, 2, 2, 3

-- INTERSECT: Promoted in BOTH years
SELECT emp_id FROM current_year_promotions
INTERSECT DISTINCT
SELECT emp_id FROM prior_year_promotions;  -- Returns: 2

-- EXCEPT (MINUS): Promoted THIS year but NOT prior year
SELECT emp_id FROM current_year_promotions
EXCEPT DISTINCT
SELECT emp_id FROM prior_year_promotions;  -- Returns: 1

```

---

**Interview Traps & Dialect Mapping**

| Operation / Concept | BigQuery Syntax | Key Interview Nuance |
| --- | --- | --- |
| **`EXCEPT` vs `MINUS**` | `EXCEPT DISTINCT` | Oracle/PostgreSQL use `MINUS`/`EXCEPT`; BigQuery requires `EXCEPT DISTINCT` (or `EXCEPT ALL`). |
| **`UNION` Default** | `UNION DISTINCT` | In BigQuery, `UNION` defaults to `UNION DISTINCT`, triggering an expensive distributed shuffle/sort. Always prefer `UNION ALL` unless deduplication is required. |
| **`LEFT JOIN` Nullification** | `WHERE right_table.col = 'val'` | Moving a right-table filter to the `WHERE` clause eliminates non-matching left rows, breaking outer join behavior. |