**Core Concepts**

* **Slot:** BigQuery's unit of computing power (CPU and memory) required to execute SQL queries. One slot roughly equals one vCPU.
* **Reservation:** A pool of dedicated slots purchased or committed in advance, assigned to specific projects or teams to guarantee performance and cost control.
* **Autoscaling:** A feature that automatically scales the number of active slots up or down within a reservation based on real-time query demand.

**Parallelism and Concurrency**

* **Parallelism:** BigQuery splits a single large query into smaller tasks and distributes them across multiple slots to execute simultaneously.
* **Concurrency:** The ability to run multiple independent queries at the same time. If active queries exceed available slots, excess queries wait in a queue.

**Monitoring Slot Usage**

* Track consumption using **Cloud Monitoring** dashboards or by querying `INFORMATION_SCHEMA.JOBS_BY_PROJECT`.
* Monitor **Slot Utilization** and **Slot Contention** to identify if your workload requires more reserved capacity or query optimization.

**Practical Example**

* **Setup:** You purchase a baseline reservation of **100 slots** with autoscaling enabled up to a maximum of **500 slots**.
* **Action:** Daily reporting runs smoothly using ~50 slots. Suddenly, a heavy analytical query drops, requiring high **parallelism** (300 slots).
* **Result:** BigQuery **autoscales** your capacity instantly from 100 to 300 slots to finish the query rapidly, then scales back down to baseline once the job completes, preventing queue delays.