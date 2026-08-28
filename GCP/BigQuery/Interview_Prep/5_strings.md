**Input Sample Dataset**

```sql
WITH customer_logs AS (
  SELECT 1 AS id, '  john.doe@company.com  ' AS raw_email, 'ORD-98765-US' AS order_code, 'apple,banana,orange' AS items UNION ALL
  SELECT 2,       '  JANE.SMITH@DOMAIN.ORG ',         'ORD-12345-EU',                  'milk,bread' UNION ALL
  SELECT 3,       'invalid_user_at_test.com',       'ORD-55555-APAC',                'laptop'
)

```

---

**1. Substrings & Trimming**

Used to extract slices of text and clean surrounding whitespace or unwanted characters.

* **`TRIM(val)`**, **`LTRIM(val)`**, **`RTRIM(val)`**: Strip leading and/or trailing whitespace (or specific characters).
* **`SUBSTR(val, start_pos, [length])`**: Extracts a substring (1-indexed). BigQuery also aliases this as `SUBSTRING()`.
* **`LEFT(val, n)` / `RIGHT(val, n)**`: Extracts $n$ characters from start or end.

```sql
SELECT
  id,
  TRIM(raw_email)                       AS cleaned_email,
  LTRIM(raw_email)                      AS left_trimmed_email,
  SUBSTR(order_code, 5, 5)              AS order_number,    -- extracts '98765'
  LEFT(order_code, 3)                   AS order_prefix,    -- extracts 'ORD'
  RIGHT(order_code, 2)                  AS order_suffix     -- extracts 'US' / 'EU'
FROM customer_logs;

```

---

**2. Search & Replace (Basic & Regex)**

Locating positions, replacing strings, and matching patterns.

* **`INSTR(val, search_str)`**: Returns the 1-indexed position of a substring (returns `0` if not found). In BigQuery, `STRPOS(val, search_str)` is the standard equivalent to ANSI `POSITION()`.
* **`REPLACE(val, from, to)`**: Exact character substitution.
* **`REGEXP_CONTAINS(val, regex)`**: Returns boolean (`TRUE`/`FALSE`). BigQuery equivalent of `REGEXP_LIKE()`.
* **`REGEXP_EXTRACT(val, regex)`**: Captures the first regex match or capture group `(...)`.

```sql
SELECT
  id,
  STRPOS(raw_email, '@')                                 AS at_symbol_pos,
  INSTR(raw_email, '@')                                  AS at_symbol_pos_instr,
  REPLACE(order_code, 'ORD-', 'ID-')                     AS formatted_order_code,
  -- Check for valid email pattern
  REGEXP_CONTAINS(TRIM(raw_email), r'^[\w\.-]+@[\w\.-]+\.\w+$') AS is_valid_email,
  -- Extract domain using regex capture group
  REGEXP_EXTRACT(TRIM(raw_email), r'@([\w\.-]+)')        AS email_domain
FROM customer_logs;

```

---

**3. Concatenation, Aggregation & Splitting**

Merging strings, group-level aggregations, and expanding delimited lists into rows/arrays.

* **`CONCAT(s1, s2, ...)`** or `||`: Combines strings. (Returns `NULL` if any argument is `NULL` in standard SQL).
* **`CONCAT_WS(separator, s1, s2, ...)`**: Combines strings with a designated delimiter, ignoring `NULL` values.
* **`STRING_AGG(col, delimiter [ORDER BY ...])`**: Aggregates column values across grouped rows into a single string (BigQuery standard for `LISTAGG` / `GROUP_CONCAT`).
* **`SPLIT(val, delimiter)`**: Splits a string into a BigQuery `ARRAY`. To expand into rows (equivalent to `STRING_SPLIT`), pair with `UNNEST()`.

```sql
-- 1. Concatenation & Array Splitting
SELECT
  id,
  CONCAT('User: ', TRIM(raw_email))             AS user_label,
  CONCAT_WS(' | ', id, order_code, items)       AS pipeline_summary,
  SPLIT(items, ',')                             AS items_array
FROM customer_logs;

-- 2. STRING_AGG: Group Aggregation across rows
SELECT 
  STRING_AGG(order_code, ' ; ' ORDER BY id)     AS all_orders_csv
FROM customer_logs;

-- 3. UNNEST(SPLIT(...)): Expanding delimited items into individual rows
SELECT 
  id,
  item
FROM customer_logs,
UNNEST(SPLIT(items, ',')) AS item;

```

---

**Interview Traps & Dialect Mapping**

| Standard / Other Dialects | BigQuery Equivalent | Key Difference |
| --- | --- | --- |
| **`POSITION(a IN b)`** | `STRPOS(b, a)` or `INSTR(b, a)` | BigQuery uses `STRPOS(haystack, needle)` (arg order is reversed from ANSI `POSITION`). |
| **`REGEXP_LIKE()`** | `REGEXP_CONTAINS()` | BigQuery uses `REGEXP_CONTAINS` to return a boolean match. |
| **`LISTAGG()` / `GROUP_CONCAT()**` | `STRING_AGG()` | BigQuery requires `STRING_AGG(val, delimiter)`. |
| **`STRING_SPLIT(val, sep)`** | `CROSS JOIN UNNEST(SPLIT(val, sep))` | `SPLIT()` produces an array; `UNNEST()` flattens it into multiple table rows. |
| **Indexing** | 1-based indexing | `SUBSTR` and `STRPOS` start at index `1`, not `0`. |