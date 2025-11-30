## 🛠️ Setup and Initialization

First, you need to set up the client connection. This assumes you have the `google-cloud-firestore` library installed (`pip install google-cloud-firestore`) and your application is correctly authenticated (e.g., using Application Default Credentials).

```python
from google.cloud import firestore

# Initialize the Firestore client
# This client automatically looks for authentication credentials
db = firestore.client()

# Define the collection we'll work with
collection_ref = db.collection('products')
```

-----

## ➕ Create (Write Data)

There are two primary ways to create a document: specifying your own ID or letting Firestore generate one automatically.

| Method | Description |
| :--- | :--- |
| **`set()`** | Creates a document with a **specific ID**. If a document with that ID already exists, it will be overwritten (or merged if the `merge=True` option is used). |
| **`add()`** | Creates a document with a **randomly generated, unique ID**. This is typically the preferred method when the document ID is not meaningful to your application. |

```python
# 1. Create with a Specific ID (using set)
doc_ref_1 = collection_ref.document('laptop_123')
doc_ref_1.set({
    'name': 'Laptop Pro X',
    'price': 1500.99,
    'in_stock': True
})
print("Document 'laptop_123' created.")

# 2. Create with an Auto-Generated ID (using add)
data = {
    'name': 'Wireless Mouse',
    'price': 25.00,
    'in_stock': True
}
update_time, doc_ref_2 = collection_ref.add(data)
print(f"Document '{doc_ref_2.id}' created.")
```

-----

## 🔎 Read (Retrieve Data)

You can retrieve data for a single document or query an entire collection.

### Get a Single Document

```python
# Get the document we created with the specific ID
doc_ref = collection_ref.document('laptop_123')

try:
    doc = doc_ref.get()
    if doc.exists:
        print(f"\nDocument data: {doc.to_dict()}")
    else:
        print("No such document!")
except Exception as e:
    print(f"An error occurred: {e}")
```

### Query a Collection (Get Multiple Documents)

```python
# Query for all products where 'price' is greater than 1000
query_ref = collection_ref.where('price', '>=', 1000.00).stream()

print("\n--- Query Results (Price >= 1000) ---")
for doc in query_ref:
    print(f"{doc.id} => {doc.to_dict()}")
```

-----

## ✏️ Update (Modify Data)

The `update()` method is used to modify one or more fields of an existing document **without overwriting the entire document**.

```python
# Get a reference to the laptop document
doc_ref = collection_ref.document('laptop_123')

# Update the price and mark it as out of stock
doc_ref.update({
    'price': 1450.00, # New price
    'in_stock': False,
    'last_updated': firestore.SERVER_TIMESTAMP # Use a server-side timestamp
})

print("\nDocument 'laptop_123' updated.")
```

-----

## ❌ Delete (Remove Data)

You can delete an entire document or just a specific field within a document.

### Delete a Document

```python
# Delete the document with the specific ID
collection_ref.document('laptop_123').delete()
print("\nDocument 'laptop_123' deleted.")
```

### Delete a Field

To delete a specific field while keeping the rest of the document, you use `firestore.DELETE_FIELD`.

```python
# Assuming 'Wireless Mouse' still exists, let's remove its 'in_stock' field
# (We use doc_ref_2 from the Create section, assuming it was successfully created)
# If not, use:
# mouse_doc_ref = collection_ref.document('<ID_of_Wireless_Mouse>') 

# mouse_doc_ref.update({
#     'in_stock': firestore.DELETE_FIELD
# })
# print("The 'in_stock' field was deleted from the Wireless Mouse document.")
```

-----

## 📦 Batch Writes

A batch write allows you to execute up to 500 write operations (create, update, or delete) atomically. This means that either **all** the operations succeed, or **none** of them do. This is crucial for maintaining data consistency.

```python
# Get a new write batch
batch = db.batch()

# 1. Create a new document in the batch
new_item_ref = collection_ref.document('headset_789')
batch.set(new_item_ref, {
    'name': 'Gaming Headset',
    'price': 79.99
})

# 2. Update a different document in the batch
# (Using the auto-generated ID document from the Create section for demonstration)
# Assuming doc_ref_2 is valid
if 'doc_ref_2' in locals():
    batch.update(doc_ref_2, {'price': 22.00})
else:
    # Use a placeholder if doc_ref_2 doesn't exist from the previous block
    placeholder_ref = collection_ref.document('some_other_id') 
    batch.update(placeholder_ref, {'price': 22.00})
    
# 3. Delete another document in the batch
# (We already deleted laptop_123, so let's use a new placeholder ID)
temp_delete_ref = collection_ref.document('temp_item_to_delete')
temp_delete_ref.set({'name': 'Temporary Item'}) # Must create it first outside the batch
batch.delete(temp_delete_ref)

# Commit the batch: all three operations happen together
batch.commit()
print("\nBatch operation committed successfully (Create, Update, and Delete occurred atomically).")
```

This video explains a broader Firebase/Firestore CRUD example in Python using a web framework. [Python CRUD Operation with Firestore Firebase & Flask](https://www.youtube.com/watch?v=NAD90zLMRV4)

http://googleusercontent.com/youtube_content/0
