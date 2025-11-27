## 💾 Firestore Data Model Fundamentals

At its heart, **Firestore** is a **NoSQL document database**. Unlike traditional relational databases (SQL) that use tables, rows, and columns, Firestore organizes data in **documents** and **collections**.

---

### 1. Documents (The Record)

A **Document** is the fundamental unit of storage in Firestore. It's essentially a lightweight record containing a set of **key-value pairs**, which are the data fields.

* **Structure:** Documents are similar to **JSON objects**.
* **Identification:** Each document is uniquely identified by its **Document ID** (either auto-generated or custom).
* **Example:** A document might represent a single user, a blog post, or a product.

| Field (Key) | Value |
| :--- | :--- |
| `name` | "Alice Johnson" |
| `email` | "alice@example.com" |
| `age` | 30 |

---

### 2. Collections (The Container)

A **Collection** is a container for **Documents**. Every document must reside in a collection.

* **Structure:** A collection is the fundamental way to organize and query your data.
* **Naming:** Collection names must be strings.
* **Analogy:** You can think of a collection like a folder, and the documents inside it as files.
* **Example:** A collection named `users` would contain all the individual user documents.

---

### 3. Sub-collections (Nesting Data)

A **Sub-collection** is a collection that is associated with a **specific Document**. They are a primary way to structure hierarchical or nested data in Firestore.

* **Hierarchy:** The data model follows a strict hierarchy: **Collection > Document > Sub-collection > Document...**
* **Nesting:** Sub-collections allow you to nest related data indefinitely, but they are *not* the same as nesting data fields *within* a document. Sub-collections keep the data logically separate and scalable.
* **Example:**
    * `users` (Collection)
        * `alice_doc_id` (Document)
            * `orders` (Sub-collection)
                * `order_101` (Document)
    * This is typically used for data that might grow very large or needs its own querying capabilities (like comments on a post).



---

### 4. Reference Types (Linking Data)

**Reference Types** are a specific data type used within a document to link to another document or collection. They are critical for establishing relationships between different parts of your database, similar to foreign keys in a relational database.

* **DocumentReference:** A field whose value is the full path to another **Document**. This is the primary way to define **one-to-one** or **one-to-many** relationships in Firestore.
    * *Example:* A `post` document might have an `authorRef` field of type `DocumentReference` pointing to a document in the `users` collection.
* **CollectionReference:** A field whose value is the path to a **Collection**. While less common for direct relationships, it's used internally and when building queries.

---

### 5. Supported Data Types

Firestore supports a wide range of data types within a document's fields:

| Data Type | Description |
| :--- | :--- |
| **String** | Any text. |
| **Number** | Includes integers and floating-point numbers. |
| **Boolean** | `true` or `false`. |
| **Timestamp** | A point in time (often auto-generated for creation/update). |
| **GeoPoint** | A latitude/longitude pair for geographical data. |
| **Blob** | Binary data. |
| **Null** | A field with no assigned value. |
| **Array** | An ordered, indexed list of values. |
| **Map** | A lightweight, nested object (dictionary) within a document. |
| **Reference** | A `DocumentReference` path to another document (see Section 4). |