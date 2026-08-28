```sql
-- Sample Input Data
WITH sales_data AS (
    SELECT * FROM (VALUES
        (101, 'Electronics', 'Laptop', 1000, '2024-01-01'::DATE),
        (102, 'Electronics', 'Phone',   800, '2024-01-02'::DATE),
        (103, 'Electronics', 'Tablet',  800, '2024-01-03'::DATE),
        (104, 'Electronics', 'Watch',   300, '2024-01-04'::DATE),
        (105, 'Furniture',   'Desk',    450, '2024-01-01'::DATE),
        (106, 'Furniture',   'Chair',   150, '2024-01-02'::DATE),
        (107, 'Furniture',   'Lamp',    150, '2024-01-03'::DATE)
    ) AS t(order_id, department, product, amount, order_date)
)

SELECT
    order_id,
    department,
    product,
    amount,
    order_date,

    -- ==========================================
    -- 1. RANKING FUNCTIONS
    -- ==========================================
    -- Strict sequential integer without gaps (1, 2, 3, 4)
    ROW_NUMBER() OVER(PARTITION BY department ORDER BY amount DESC) AS row_num,

    -- Shared rank for ties with gaps (1, 2, 2, 4)
    RANK() OVER(PARTITION BY department ORDER BY amount DESC) AS rnk,

    -- Shared rank for ties without gaps (1, 2, 2, 3)
    DENSE_RANK() OVER(PARTITION BY department ORDER BY amount DESC) AS dense_rnk,

    -- Splits partition into n roughly equal buckets (1, 2)
    NTILE(2) OVER(PARTITION BY department ORDER BY amount DESC) AS ntile_bucket,

    -- ==========================================
    -- 2. VALUE OFFSET FUNCTIONS
    -- ==========================================
    -- Value from the previous row (offset = 1, default = 0)
    LAG(amount, 1, 0) OVER(PARTITION BY department ORDER BY order_date ASC) AS prev_amount,

    -- Value from the next row
    LEAD(amount, 1, 0) OVER(PARTITION BY department ORDER BY order_date ASC) AS next_amount,

    -- First value in the current window frame
    FIRST_VALUE(product) OVER(
        PARTITION BY department 
        ORDER BY order_date ASC
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS first_product_ordered,

    -- Last value in the current window frame (Requires explicit frame to look ahead)
    LAST_VALUE(product) OVER(
        PARTITION BY department 
        ORDER BY order_date ASC
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS last_product_ordered,

    -- Specific nth value in the window frame (2nd ordered product)
    NTH_VALUE(product, 2) OVER(
        PARTITION BY department 
        ORDER BY order_date ASC
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS second_product_ordered,

    -- ==========================================
    -- 3. FRAMING & BOUNDARIES
    -- ==========================================
    -- Cumulative Running Total (Default frame when ORDER BY is present: RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
    SUM(amount) OVER(
        PARTITION BY department 
        ORDER BY order_date ASC
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total_rows,

    -- Moving Average: 1 row before, current row, 1 row after (Physical rows)
    AVG(amount) OVER(
        PARTITION BY department 
        ORDER BY order_date ASC
        ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
    ) AS moving_avg_3rows,

    -- Range-based frame: Evaluates value duplicates identically (Logical offsets)
    SUM(amount) OVER(
        PARTITION BY department 
        ORDER BY amount ASC
        RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS range_running_total

FROM sales_data;
```

**Key Takeaways:**

* **`ROWS` vs `RANGE**`: `ROWS` treats duplicate values in `ORDER BY` individually; `RANGE` groups duplicate values together in the frame.
* **Default Frame**: An `ORDER BY` clause defaults to `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`.
* **Lookahead Functions**: `LAST_VALUE()` and `NTH_VALUE()` require `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING` to avoid stopping at `CURRENT ROW`.
