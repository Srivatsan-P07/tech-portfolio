# **Intermediate Cypher** concepts

---

### 🔗 1. **CREATE Relationships**

* **Purpose** : Connect nodes with relationships to show how entities are related.

#### 🔹 Syntax:

```cypher
MATCH (a:Person {name: 'Alice'}), (b:Person {name: 'Bob'})
CREATE (a)-[:FRIENDS_WITH]->(b)
```

This connects Alice to Bob with a `FRIENDS_WITH` relationship.

#### 🔄 Direction:

* `-->` : Outgoing
* `<--` : Incoming
* `--` : Undirected

---

### ✏️ 2. **UPDATE / DELETE**

#### 🔹 UPDATE (using `SET`)

```cypher
MATCH (p:Person {name: 'Alice'})
SET p.age = 30
```

This updates Alice's age to 30.

You can also  **add new labels** :

```cypher
SET p:Employee
```

#### 🗑️ DELETE

```cypher
MATCH (p:Person {name: 'Bob'})
DELETE p
```

Deletes the node. But ⚠️ you can't delete a node if it has relationships unless you:

```cypher
MATCH (p:Person {name: 'Bob'})-[r]-()
DELETE r, p
```

---

### 📊 3. **Aggregations**

Used to summarize data (just like SQL).

#### 🔸 COUNT

```cypher
MATCH (p:Person)
RETURN COUNT(p)
```

Counts total number of `Person` nodes.

#### 🔸 SUM

```cypher
MATCH (p:Person)
RETURN SUM(p.age)
```

Adds up all the ages of `Person` nodes.

You can also combine:

```cypher
MATCH (p:Person)
RETURN p.gender, COUNT(p) AS count
```

Gives count by gender.

---

### 🧩 4. **Pattern Matching**

This is Cypher’s superpower — finding complex relationships between nodes.

#### 🔹 Example:

```cypher
MATCH (a:Person)-[:FRIENDS_WITH]->(b:Person)
RETURN a.name, b.name
```

Finds all people who are friends with other people.

#### 🔹 More complex:

```cypher
MATCH (a:Person)-[:FRIENDS_WITH]->(:Person)-[:WORKS_WITH]->(c:Person)
RETURN a.name, c.name
```

Finds people who are *friends of someone who works with someone else* — a two-hop connection.

---

.
