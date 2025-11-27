# GCP Firestore Course Content
<br>

| Module No. | Topic                                | Sub-Topics                                                                                                               | Python Examples Included          |
| ---------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | --------------------------------- |
| **1**      | **Introduction to Firestore**        | What is Firestore? • Firestore vs Realtime DB • Use cases • Firestore modes (Native vs Datastore)                        | No (conceptual)                   |
| **2**      | **Setting Up Environment**           | Create GCP project • Enable Firestore API • Install Python SDK • Service account keys • gcloud setup                     | ✔ Connecting to Firestore client  |
| **3**      | **Firestore Data Model**             | Documents • Collections • Sub-collections • Reference types • Supported data types                                       | ✔ Creating collections/documents  |
| **4**      | **Basic CRUD Operations**            | Create • Read • Update • Delete • Batch writes                                                                           | ✔ Full CRUD code                  |
| **5**      | **Queries in Firestore**             | Simple queries • Compound queries • Range filters • OrderBy • Pagination • Query limitations                             | ✔ Query examples                  |
| **6**      | **Realtime Listeners**               | Snapshot listeners • Callbacks • Streaming updates • Limitations                                                         | ✔ Python listener example         |
| **7**      | **Structured Data Modelling**        | Embedding vs referencing • Denormalization • One-to-many • Many-to-many                                                  | ✔ Sample schema design            |
| **8**      | **Transactions & Batch Operations**  | When to use transactions • Automatic retries • Atomicity • Batch writes                                                  | ✔ Transaction example             |
| **9**      | **Indexes in Firestore**             | Automatic indexes • Composite indexes • Index errors • Managing indexes                                                  | ✔ Query failing → Fix via index   |
| **10**     | **Firestore Security Rules**         | Rules syntax • Allow/deny • read/write rules • Authentication-based rules • Rules testing                                | ✔ Secure CRUD example             |
| **11**     | **Python Authentication Options**    | Service accounts • Application Default Credentials • Using Firestore from Cloud Run • Using Firestore from local machine | ✔ ADC example                     |
| **12**     | **Serverless Integrations**          | Firestore with Cloud Functions • Cloud Run • Pub/Sub triggers                                                            | ✔ Simple trigger function example |
| **13**     | **Pagination & Large Data Handling** | Offset vs Cursor • StartAfter / StartAt • Fetching 100k+ documents efficiently                                           | ✔ Pagination code                 |
| **14**     | **Performance Optimization**         | Index tuning • Avoiding hotspots • Sharding strategies • Data design patterns                                            | ✔ Example of sharded counter      |
| **15**     | **Backup, Export, Import**           | Scheduled backups • gcloud export/import • Point-in-time recovery                                                        | No (CLI focused)                  |
| **16**     | **Firestore in Production**          | Quotas • Pricing • Monitoring • Latency considerations                                                                   | No (conceptual)                   |
| **17**     | **Sample Python Project (Capstone)** | Build a full CRUD web app • Use Flask/FastAPI • Query filters • Authentication • Deployment on Cloud Run                 | ✔ End-to-end project              |
