**Capacitor (Columnar Storage)**

* **Layout:** BigQuery stores data column-by-column rather than row-by-row using its proprietary **Capacitor** (
    `Google BigQuery's proprietary columnar storage format used to store data in the underlying Colossus distributed file system`
) format.
* **Scan Efficiency:** Queries read only the specific columns needed, drastically reducing I/O and slot usage.
* **Compression:** Automatically applies compression algorithms (e.g., run-length encoding, dictionary encoding) optimized for each data type.

**Analyzing Storage Stats**

* Query BigQuery's `INFORMATION_SCHEMA` to monitor storage size, costs, and optimization.
* **Key View:** `INFORMATION_SCHEMA.TABLE_STORAGE` (or `TABLE_STORAGE_BY_PROJECT`).
* **Key Metrics:**
* `total_logical_bytes`: Uncompressed size of active and long-term storage.
* `active_logical_bytes`: Data modified within the last 30 days.
* `long_term_logical_bytes`: Data unmodified for 30+ days (automatically discounted by 50%).


* **Example Query:**
```sql
SELECT table_id, total_logical_bytes / POW(10,9) AS size_gb
FROM `project.dataset.INFORMATION_SCHEMA.TABLE_STORAGE`;

```