Cypher is the query language for querying graph databases like Neo4j. Here's a breakdown of the basics:

### 1. **CREATE**

* **Purpose** : Used to create nodes and relationships in the graph database.
* **Syntax** :

```cypher
  CREATE (node_name:Label {property: value})
```

  Example:

```cypher
  CREATE (node1:Person {name: 'John', age: 25})
```

  This creates a node with the label `Person` and properties `name` and `age`.

### 2. **MATCH**

* **Purpose** : Used to search for existing nodes and relationships.
* **Syntax** :

```cypher
  MATCH (node_name:Label {property: value})
```

  Example:

```cypher
  MATCH (node1:Person {name: 'John'})
  RETURN node1
```

  This searches for a node with the label `Person` and the name property equal to 'John'.

### 3. **RETURN**

* **Purpose** : Used to return results from a query, like nodes or relationships.
* **Syntax** :

```cypher
  RETURN node_name
```

  Example:

```cypher
  MATCH (a:Person {name: 'John'})
  RETURN a
```
This returns the node with the name 'John'.

**Select All**

```cypher
  MATCH (n) RETURN n;
  MATCH (n) RETURN n LIMIT 100;
  MATCH (n) RETURN labels(n), properties(n);
```

### 4. **WHERE**

* **Purpose** : Used to filter results based on conditions.
* **Syntax** :

```cypher
  WHERE condition
```

  Example:

```cypher
  MATCH (a:Person)
  WHERE a.age > 30
  RETURN a
```

  This returns all `Person` nodes where the age is greater than 30.

### 5. **AND / OR**

* **Purpose** : Used to combine multiple conditions in a `WHERE` clause.
* `AND`: Both conditions must be true.
* `OR`: Either condition can be true.
* **Syntax** :

```cypher
  WHERE condition1 AND condition2
  WHERE condition1 OR condition2
```

  Example:

```cypher
  MATCH (a:Person)
  WHERE a.age > 30 
  AND a.name = 'John'
  RETURN a
```

  This returns the `Person` nodes where age is greater than 30 *and* the name is 'John'.

```cypher
  MATCH (a:Person)
  WHERE a.age > 30 OR a.name = 'John'
  RETURN a
```

  This returns `Person` nodes where age is greater than 30 *or* the name is 'John'.

### 6. **LIMIT**

* **Purpose** : Limits the number of results returned.
* **Syntax** :

```cypher
  LIMIT number
```

  Example:

```cypher
  MATCH (a:Person)
  RETURN a
  LIMIT 5
```

  This returns only the first 5 results.

### 7. **ORDER BY**

* **Purpose** : Orders the results by a specific property.
* **Syntax** :

```cypher
  ORDER BY property
```

  Example:

```cypher
  MATCH (a:Person)
  RETURN a
  ORDER BY a.age DESC
```

  This orders the `Person` nodes by age in descending order.

---

These are some of the fundamental components to create, query, and filter data in Cypher. You can combine them in various ways to perform more complex queries.
