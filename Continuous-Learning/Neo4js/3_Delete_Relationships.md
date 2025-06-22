# **delete a relationship** in Neo4j

---

### 🔹 Delete a specific relationship between nodes

```cypher
MATCH (a:Person {name: 'Alice'})-[r:FRIENDS_WITH]->(b:Person {name: 'Bob'})
DELETE r;
```

This deletes the `FRIENDS_WITH` relationship  **from Alice to Bob** , but keeps both nodes.

---

### 🔹 Delete all relationships of a certain type

```cypher
MATCH ()-[r:FRIENDS_WITH]->()
DELETE r;
```

This deletes **all `FRIENDS_WITH` relationships** in the graph.

---

### 🔹 Delete **all** relationships (regardless of type)

```cypher
MATCH ()-[r]->()
DELETE r;
```

Use this carefully—it removes **every relationship** in the database.

---

# **delete all relationships of a single person (or node)** in Neo4j

### 🔹 Delete all relationships of one node (incoming and outgoing)

```cypher
MATCH (p:Person {name: 'Alice'})-[r]-()
DELETE r;
```

* This matches `Alice` and **any relationship** (`-[]-`) connected to her.
* It deletes the relationships only— **not the node itself** .

---

### 🔹 Optional: If you only want to delete **outgoing** or **incoming** relationships:

* **Outgoing only** :

```cypher
  MATCH (p:Person {name: 'Alice'})-[r]->()
  DELETE r;
```

* **Incoming only** :

```cypher
  MATCH ()-[r]->(p:Person {name: 'Alice'})
  DELETE r;
```


# **Many-to-one relationship** in Neo4j

---

### 🔹 Example: Two people work at the same company

```cypher
CREATE (a:Person {name: 'Alice'}),
       (b:Person {name: 'Bob'}),
       (c:Company {name: 'Acme Corp'}),
       (a)-[:WORKS_AT]->(c),
       (b)-[:WORKS_AT]->(c);
```

Now:

* Alice and Bob are each connected **to** Acme Corp.
* This is a **many-to-one** (`Person` ➡ `Company`) relationship.

---

### 🔸 You can also build this with `UNWIND` (bulk insert style):

```cypher
CREATE (company:Company {name: 'Acme Corp'});

UNWIND ['Alice', 'Bob'] AS personName
CREATE (p:Person {name: personName})
CREATE (p)-[:WORKS_AT]->(company);
```

---

Want to go deeper and add properties to the relationships or model one-to-many the other way around?
