**Input Sample Dataset**

```sql
WITH customer_orders AS (
  SELECT 1 AS order_id, 100 AS actual_amount, 100 AS expected_amount, 'VIP' AS tier,        'card' AS payment_method UNION ALL
  SELECT 2,             0,                    50,                     'Standard',   NULL                     UNION ALL
  SELECT 3,             NULL,                 75,                     NULL,         'paypal'                 UNION ALL
  SELECT 4,             NULL,                 NULL,                   'Standard',   NULL
)

```

---

**1. Branching Logic**

* **`CASE WHEN ... THEN ... ELSE ... END`**: Standard ANSI branching for multi-condition logic (evaluates sequentially top-to-bottom).
* **`IF(condition, true_val, false_val)`**: Ternary inline shorthand (BigQuery's built-in equivalent to T-SQL's `IIF()`).

```sql
SELECT
  order_id,
  -- Multi-branch evaluation
  CASE 
    WHEN tier = 'VIP' THEN actual_amount * 0.8
    WHEN tier = 'Standard' THEN actual_amount * 0.95
    ELSE actual_amount
  END AS discounted_amount,
  
  -- Inline ternary branch
  IF(payment_method IS NOT NULL, payment_method, 'unpaid') AS payment_status
FROM customer_orders;

```

---

**2. Null Handling**

* **`COALESCE(val1, val2, ...)`**: Returns the **first non-null** value from an arbitrary list of arguments.
* **`IFNULL(val, default_val)`**: Shorthand for two arguments; returns `default_val` if `val` is `NULL`.
* **`NULLIF(val1, val2)`**: Returns `NULL` if $val1 = val2$; otherwise returns $val1$ (prevents **division-by-zero** errors).
* **`IS DISTINCT FROM`**: NULL-safe comparison operator. Treats two `NULL`s as equal (`NULL IS DISTINCT FROM NULL` evaluates to `FALSE`).

```sql
SELECT
  order_id,
  -- 1. First non-null fallback chain
  COALESCE(actual_amount, expected_amount, 0) AS final_billed_amount,
  
  -- 2. Two-argument null replacement
  IFNULL(tier, 'Guest') AS customer_tier,
  
  -- 3. Prevent division by zero: if actual_amount is 0, NULLIF turns it to NULL -> expression yields NULL
  expected_amount / NULLIF(actual_amount, 0) AS variance_ratio,
  
  -- 4. NULL-safe inequality: returns TRUE only if values truly differ (handles NULLs safely)
  actual_amount IS DISTINCT FROM expected_amount AS amounts_differ
FROM customer_orders;

```

---

**Interview Traps & Dialect Mapping**

| Function / Syntax | BigQuery Standard | Interview Note |
| --- | --- | --- |
| **`IIF(cond, t, f)`** | `IF(cond, t, f)` | `IIF()` is T-SQL / MS Access; BigQuery uses `IF()`. |
| **`ISNULL(a, b)`** | `IFNULL(a, b)` or `COALESCE(a, b)` | T-SQL uses `ISNULL(a, b)`. In SQL standards / BigQuery, `IS NULL` is a predicate, whereas `IFNULL()` is the replacement function. |
| **`NULLIF` Trick** | `a / NULLIF(b, 0)` | Standard method to avoid `Division by zero` runtime query failures. |
| **`=` vs `IS NOT DISTINCT FROM**` | `a IS NOT DISTINCT FROM b` | Regular equality `a = b` yields `NULL` (unknown) if either operand is `NULL`. `IS NOT DISTINCT FROM` returns `TRUE` if both operands are `NULL`. |