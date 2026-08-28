**Input Sample Dataset**

```sql
WITH orders AS (
  SELECT 101 AS order_id, 1 AS customer_id, DATE '2026-01-15' AS order_date, 250 AS amount, 'delivered' AS status UNION ALL
  SELECT 102,             1,                 DATE '2026-02-10',                150,    'delivered'          UNION ALL
  SELECT 103,             2,                 DATE '2026-02-12',                500,    'pending'            UNION ALL
  SELECT 104,             3,                 DATE '2026-03-01',                50,     'cancelled'
),
customers AS (
  SELECT 1 AS customer_id, 'Alice' AS name, 'US' AS region UNION ALL
  SELECT 2,               'Bob',   'US'                   UNION ALL
  SELECT 3,               'Carol', 'EU'
)

```

---

**1. Execution Analysis (`EXPLAIN` vs `EXPLAIN ANALYZE`)**

* **`EXPLAIN`**: Generates the **estimated query plan** based on optimizer statistics without executing the query (shows estimated cost/rows).
* **`EXPLAIN ANALYZE`**: Actually **runs the query** and outputs the physical execution profile (actual run time, memory used, rows processed at each stage).
* *BigQuery Note*: In BigQuery, this is exposed via the **Execution Graph / Information Schema** (e.g., `INFORMATION_SCHEMA.JOBS_BY_*`) showing slot time, shuffle bytes, and stage bottlenecks (Read, Compute, Write).

```sql
-- Standard RDBMS syntax:
-- EXPLAIN ANALYZE
SELECT c.name, SUM(o.amount) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.name;

```

---

**2. Indexing Mechanics & SARGability**

* **B-Tree Index**: Balanced tree structure optimized for equality (`=`) and range scans (`<`, `>`, `BETWEEN`).
* **Clustered vs. Non-Clustered**:
* *Clustered Index*: Dictates the physical storage order of the rows on disk (only one per table). In BigQuery, this corresponds to **Table Partitioning & Clustering**.
* *Non-Clustered Index*: A separate structure storing pointers/row IDs back to the base table.


* **Composite Index**: Multi-column index; follows the **Leftmost Prefix Rule** (an index on `(region, status)` speeds up searches on `region` or `region + status`, but not `status` alone).
* **SARGability (Search Argument Able)**: Writing predicates that allow index scans instead of full-table scans. Applying functions to columns in `WHERE` breaks SARGability.

```sql
-- ❌ NON-SARGable: Wrapping the indexed column in a function forces a Full Table Scan
SELECT order_id, amount
FROM orders
WHERE EXTRACT(YEAR FROM order_date) = 2026;

-- ✅ SARGable: Column is isolated, allowing direct index seeks / partition pruning
SELECT order_id, amount
FROM orders
WHERE order_date >= DATE '2026-01-01' 
  AND order_date < DATE '2027-01-01';

```

---

**3. Optimization Pitfalls**

**Pitfall A: Correlated Subqueries vs. Joins**

* *Issue*: Correlated subqueries execute once per outer row in row-by-row engines, degrading to $O(M \times N)$ complexity.

```sql
-- ❌ BAD: Evaluates subquery for every customer row
SELECT 
  c.name,
  (SELECT SUM(o.amount) FROM orders o WHERE o.customer_id = c.customer_id) AS total_spent
FROM customers c;

-- ✅ GOOD: Aggregates once via LEFT JOIN
SELECT 
  c.name,
  COALESCE(SUM(o.amount), 0) AS total_spent
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name;

```

**Pitfall B: Unintentional Cartesian Products (`CROSS JOIN`)**

* *Issue*: Missing or poorly defined join predicates multiply row counts exponentially, blowing up memory and shuffle limits.

```sql
-- ❌ BAD: Missing join condition causes M x N row explosion
SELECT c.name, o.amount
FROM customers c, orders o;

-- ✅ GOOD: Explicit deterministic join key
SELECT c.name, o.amount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id;

```

**Pitfall C: Cargo-Cult / Unnecessary `DISTINCT**`

* *Issue*: Slapping `DISTINCT` on queries hides bad joins and forces an expensive global hash aggregation/sort across nodes.

```sql
-- ❌ BAD: Using DISTINCT to deduplicate fan-out caused by an un-aggregated join
SELECT DISTINCT c.customer_id, c.name
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id;

-- ✅ GOOD: Use EXISTS to check presence without creating duplicate rows to sort
SELECT c.customer_id, c.name
FROM customers c
WHERE EXISTS (
  SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id
);

```

---

**Performance Concept Cheat Sheet**

| Concept | Anti-Pattern | Optimized Pattern | Reason |
| --- | --- | --- | --- |
| **SARGability** | `WHERE DATE(ts) = '2026-01-01'` | `WHERE ts >= '...' AND ts < '...'` | Function wrappers prevent index seek/partition pruning. |
| **Row Multiplication** | `SELECT DISTINCT` after 1:N join | Pre-aggregate or use `EXISTS` / `IN` | Eliminates expensive distributed deduplication step. |
| **Subquery Loops** | Scalar subquery in `SELECT` | Set-based `LEFT JOIN ... GROUP BY` | Converts row-by-row operations into bulk relational scans. |
| **Composite Index** | Index on `(A, B)`, queried on `B` | Query on `(A)` or `(A, B)` | Leftmost prefix rule dictates tree lookup entry point. |