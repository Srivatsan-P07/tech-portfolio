**Isolation Models**

* **Shared Table + Authorized Views / Row-Level Security (RLS):** Store all tenant data in a single table with a `tenant_id` column. Use BigQuery Authorized Views or RLS policies to restrict users to rows matching their specific tenant ID.
* **Dataset-per-Tenant:** Isolate data physically into separate datasets per client. Ideal for strict regulatory compliance or limited tenant counts.

**SLAs and Compute Allocation**

* **Slot Reservations:** Use BigQuery Editions (Enterprise or Enterprise Plus) to purchase dedicated baseline slots. Assign these reservations to specific tenants or workloads to prevent "noisy neighbor" performance degradation.
* **Uptime SLA:** BigQuery Enterprise and Enterprise Plus tiers provide a financial-backed $99.99\%$ monthly uptime SLA.

**Example: Multi-Tenant Setup via Authorized Views**

```sql
-- 1. Base table with all tenant data (restricted access)
CREATE TABLE `my-project.base_data.orders` (
  order_id STRING,
  tenant_id STRING,
  amount NUMERIC
);

-- 2. Create an isolated view for Tenant A
CREATE VIEW `my-project.tenant_a.orders` AS
SELECT order_id, amount
FROM `my-project.base_data.orders`
WHERE tenant_id = 'tenant_a';

-- 3. Authorize the view to read from base_data without granting direct table access

```