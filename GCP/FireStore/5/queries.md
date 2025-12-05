## 🧐 Queries in Firestore

A **Firestore query** is a method of retrieving documents from a collection that match specific criteria. Queries are always executed against a single collection or a collection group.

### 1\. Simple Queries

A simple query retrieves all documents from a collection or uses a single equality filter (e.g., where a field equals a specific value).

**Example: Get all documents**

```python
# Get all documents in the 'products' collection
docs = collection_ref.stream()

print("--- All Products ---")
for doc in docs:
    print(f"{doc.id} => {doc.to_dict()}")
```

**Example: Filter by equality**

```python
# Query: Get all products where 'category' is 'Electronics'
query = collection_ref.where(field_path='category', op_string='==', value='Electronics')
electronics_docs = query.stream()

print("\n--- Electronics Products ---")
for doc in electronics_docs:
    print(f"{doc.id} => {doc.to_dict()}")
```

-----

### 2\. Compound Queries

A compound query uses **multiple filters** in a single query. All filters in the query must be satisfied for a document to be returned.

**Note:** Firestore can only perform range/inequality filters (like $<$, $<=$, $>$, $>=$, `in`, `not_in`, `array_contains_any`) on **one field** per query. All other filters must be equality filters.

**Example: Multiple equality filters**

```python
# Query: Get products where 'category' is 'Books' AND 'in_stock' is True
query = (
    collection_ref
    .where('category', '==', 'Books')
    .where('in_stock', '==', True)
)
book_docs = query.stream()

print("\n--- In-Stock Books ---")
for doc in book_docs:
    print(f"{doc.id} => {doc.to_dict()}")
```

-----

### 3\. Range Filters

Range filters are used to query for documents where a field falls within a specified range. They include comparison operators like $<$, $<=$, $>$, and $>=$.

**Example: Filter by price range**

```python
# Query: Get products where 'price' is greater than 50.00
query = collection_ref.where('price', '>', 50.00)
expensive_docs = query.stream()

print("\n--- Products > $50.00 ---")
for doc in expensive_docs:
    print(f"{doc.id} => {doc.to_dict()}")
```

**Example: Using the `in` operator (an equality range filter)**

The `in` operator finds documents where a field's value is equal to **any** of the values in the provided list.

```python
# Query: Get products where 'color' is 'Red' OR 'Blue' OR 'Green'
query = collection_ref.where('color', 'in', ['Red', 'Blue', 'Green'])
color_docs = query.stream()

print("\n--- Red, Blue, or Green Products ---")
for doc in color_docs:
    print(f"{doc.id} => {doc.to_dict()}")
```

-----

### 4\. OrderBy

The `order_by()` method sorts the results of a query based on the values of a specified field, either in ascending (default) or descending order.

**Example: Order by price, ascending**

```python
# Query: Get all products, ordered by 'price' low to high
query = collection_ref.order_by('price')
ordered_docs = query.stream()

print("\n--- Products Ordered by Price (Low to High) ---")
for doc in ordered_docs:
    print(f"Price: {doc.get('price'):<8} | {doc.id} => {doc.to_dict().get('name')}")
```

**Example: Order by category (ascending) and then price (descending)**

You can sort by multiple fields.

```python
from google.cloud.firestore import Query

# Sort by 'category' ascending, then by 'price' descending
query = (
    collection_ref
    .order_by('category', direction=Query.ASCENDING)
    .order_by('price', direction=Query.DESCENDING)
)
compound_order_docs = query.stream()
```

-----

### 5\. Pagination

Pagination is used to retrieve results in manageable chunks, which is essential for large datasets. It uses the methods `limit()`, `start_after()`/`start_at()`, and `end_before()`/`end_at()`.

#### A. Limiting and Offsetting

  * **`limit(N)`**: Restricts the number of documents returned to $N$.
  * **Firestore does not have a direct `offset()` method** because it performs poorly on large datasets. Instead, you use **cursor-based pagination** with `start_after()`.

**Example: Get the first 5 products**

```python
query = collection_ref.order_by('price').limit(5)
first_page_docs = list(query.stream())

print("\n--- Page 1 (First 5) ---")
for doc in first_page_docs:
    print(f"{doc.id} => Price: {doc.get('price')}")
```

#### B. Cursor-Based Pagination

To get the next page, you use the **last document of the current page** as a starting point.

**Example: Get the next 5 products (Page 2)**

```python
# 1. Get the last document from the first page
if first_page_docs:
    last_doc = first_page_docs[-1]

    # 2. Start the next query AFTER this document
    query_page_2 = (
        collection_ref
        .order_by('price')
        .start_after(last_doc)
        .limit(5)
    )
    second_page_docs = query_page_2.stream()

    print("\n--- Page 2 (Next 5) ---")
    for doc in second_page_docs:
        print(f"{doc.id} => Price: {doc.get('price')}")
```

-----

### 6\. Query Limitations

Firestore queries are designed to be fast, but this speed is achieved by imposing a few strict limitations:

| Limitation | Description | Python Example |
| :--- | :--- | :--- |
| **Index Requirement** | Firestore requires an **index** for every query that uses a range or `order_by()` clause, or a compound query that combines filters on different fields. | If you query `.where('price', '>', 10).order_by('category')`, and an index doesn't exist, the query will fail with a link to create the required index. |
| **Single Range Field** | A query can only include a range/inequality filter ($<$, $<=$, $>$, $>=$, `in`, `not_in`, `array_contains_any`) on **a single field**. | This is **NOT** allowed: `.where('price', '>', 10).where('stock', '<', 5)` |
| **Ordering and Filtering** | If you use a range filter on a field (e.g., `price`), any `order_by()` clause **must** start with the same field. | If you query `.where('price', '>', 10)`, the next operation must be `.order_by('price')` if you plan to order. |
| **No "OR" Queries** | Firestore does not support native logical OR queries in a single query object. | You cannot do: `category == 'Book' OR category == 'Movie'`. You must use the `in` operator (e.g., `.where('category', 'in', ['Book', 'Movie'])`) or execute separate queries. |
| **`in` and `array-contains-any` Limit** | The lists provided to `in` and `array-contains-any` operators are limited to **10 values**. | `.where('color', 'in', ['A', 'B', 'C', ..., 'L'])` will fail if the list has 11 or more items. |

-----