# 🔥🏪 Firestore Data Modelling

Cloud Firestore's NoSQL document-based structure requires a different approach to data modeling than traditional relational databases. The core concepts revolve around optimizing for reads and minimizing the number of queries needed, which often involves a mix of embedding, referencing, and denormalization.

## 🏗️ Structured Data Modelling in Firestore

Firestore data is organized into **Collections** of **Documents**. Documents contain key-value pairs, which can be simple fields or complex nested objects (maps/arrays) and even pointers to other documents (Document References).

### Embedding vs. Referencing

This is the primary decision point for establishing relationships in Firestore.

| Method | Description | When to Use | Trade-offs |
| :--- | :--- | :--- | :--- |
| **Embedding** | Storing related data directly within the parent document (e.g., an array of comments or a map of basic user details). | The related data is **small**, **doesn't change often**, and is **always needed** when reading the parent document. | **Pros:** Single read operation for all data; faster reads. **Cons:** Data duplication (if embedded in multiple places); document size limit (1 MiB); updating embedded data is expensive if duplicated. |
| **Referencing** | Storing related data in a separate document/collection and using a **Document Reference** or the ID to link them (like a foreign key). | The related data is **large**, **changes frequently**, or is **not always needed** with the parent document. | **Pros:** Minimal data duplication; no document size constraint; updates are only required in one place. **Cons:** Requires multiple read operations ("joins") to fetch all related data, which can increase cost and latency. |

### Denormalization

Denormalization is the practice of **duplicating data** across multiple documents to speed up read queries and reduce the need for multiple reads (references).

  * **Example:** In a blog application, instead of only storing the `author_id` in a `posts` document (referencing), you might also store the `author_name` and `author_profile_pic` directly in the `posts` document (denormalization/embedding).
  * If the author changes their name, you would need to update the `users` document AND all of their `posts` documents, typically using a **Batched Write** or a **Cloud Function** to maintain consistency.


## 🤝 Modeling Relationships

The key to relational modeling in Firestore is deciding between **subcollections** (for strict parent-child hierarchies) and **root-level collections with references** (for flexible querying).

### 1\. One-to-Many Relationship

A single "parent" entity is related to multiple "child" entities (e.g., one **Author** has many **Posts**).

| Strategy | Structure (Example: Author $\to$ Posts) | Pros & Cons |
| :--- | :--- | :--- |
| **A. Subcollection** | `authors/{authorId}/posts/{postId}` | **Pros:** Naturally hierarchical; efficient for getting *all* posts for a single author. **Cons:** Cannot query across all posts from all authors easily (requires a Collection Group Query); posts are tightly coupled to the author. |
| **B. Root Collection + Reference** | `authors/{authorId}` and `posts/{postId}` (where `posts` has an `author_id` field) | **Pros:** Allows querying all posts in one place; flexible querying (e.g., *all* posts from a specific author). **Cons:** Requires two reads (one for the author, one for their posts) or denormalization for author details. |

### 2\. Many-to-Many Relationship

Entities on both sides of the relationship can be related to multiple entities on the other side (e.g., many **Students** can take many **Courses**). This often requires a "join" or "junction" collection.

| Strategy | Structure (Example: Students $\leftrightarrow$ Courses) | Pros & Cons |
| :--- | :--- | :--- |
| **Junction Collection** | 1. `students/{studentId}` 2. `courses/{courseId}` 3. **`enrollments/{enrollmentId}`** (with `student_id` and `course_id` fields) | **Pros:** Single source of truth for the relationship; flexible for complex queries (e.g., *all* students in a specific course, or *all* courses for a specific student). **Cons:** Requires *at least* three reads to get student details, course details, and the enrollment record. |
| **Denormalized Arrays** | `students/{studentId}` (with an array of `course_ids`) and `courses/{courseId}` (with an array of `student_ids`) | **Pros:** Faster lookups (single read). **Cons:** Arrays have query limitations (e.g., no compound querying across array elements); limits on array size; updates require a batch write to maintain consistency in two places. |
