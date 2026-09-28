**Compute-Storage Separation**

* **Colossus (Storage):** Durable, low-cost distributed file system where table data lives independently.
* **Dremel (Compute):** Stateless query execution engine that spins up thousands of workers per query.
* **Benefit:** Scale storage and compute independently without provisioning instances; pay only for data stored and queries run.

**Scale-Out Query Execution**

* **Massively Parallel Processing (MPP):** Workloads distribute across thousands of nodes simultaneously.
* **Tree Architecture:**
* **Root Server:** Receives and coordinates the SQL query.
* **Mixer Servers:** Aggregate intermediate results from lower tiers.
* **Leaf Servers:** Perform scanning, filtering, and aggregation directly on storage blocks.


* **Jupiter Network:** Google's high-speed petabit network streams data between storage and compute instantly, preventing I/O bottlenecks.

**Architecture Diagram**

```text
[ User / BI Tool ]
        │
        ▼
[ Root Server ] (Coordinates Query)
        │
        ▼
[ Mixer Servers ] (Intermediate Aggregation)
        │
        ▼
[ Leaf Servers ] (Dremel Compute Nodes) 
        │  ▲
        │  │ (Jupiter Network - Petabit Fabric)
        ▼  │
[ Colossus ] (Decoupled Distributed Storage)

```