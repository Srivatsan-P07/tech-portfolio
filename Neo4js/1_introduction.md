# **Introduction to Neo4j & Graph DBs**

Neo4j is a  **graph database** , which means it stores data in a way that's based on **graphs** rather than tables (like in SQL) or documents (like in MongoDB).

---

### **What is a Graph Database?**

A **graph database** uses a structure of:

* **Nodes** : Think of these as **entities** (like a person, product, city, etc.)
* **Relationships** : These are **connections** between nodes (e.g., "FRIENDS_WITH", "LIVES_IN", "LIKES")
* **Properties** : Both nodes and relationships can have **key-value pairs** that hold data (like name, age, date, etc.)

Example:

```
(Alice)-[:FRIENDS_WITH {since: 2022}]->(Bob)
```

* **Alice** and **Bob** are nodes
* **FRIENDS_WITH** is a relationship
* `{since: 2022}` is a property of that relationship

---

### **Why Use a Graph DB?**

Graph DBs are  **optimized for connected data** , which means they're great when relationships matter more than raw data.

---

### **Neo4j Use Cases**

Neo4j is widely used in industries for:

1. **Social Networks** – Modeling friends, followers, connections
2. **Recommendation Systems** – "People who bought this also bought..."
3. **Fraud Detection** – Find suspicious patterns quickly
4. **Network and IT Ops** – Visualizing and managing connected systems
5. **Knowledge Graphs** – Representing and querying knowledge-rich data

---

.
