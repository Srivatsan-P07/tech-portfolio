# 📦 Google Cloud Storage (GCS) - `storage.Client()` Methods Guide

This document lists and explains the **main methods** you can use with the `google-cloud-storage` Python client, specifically with the **`storage.Client()`** object.

---

## 📚 Setup

Install the library:

```bash
pip install google-cloud-storage
```

Initialize the client:

```python
from google.cloud import storage

client = storage.Client()
```

---

## 🛠️ `storage.Client()` - Main Methods

| Method                                                                | Description                                                                              | Example                                                                     |
| :-------------------------------------------------------------------- | :--------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------- |
| `list_buckets()`                                                    | Lists all buckets in the project.                                                        | `buckets = client.list_buckets()`                                         |
| `create_bucket(bucket_name, **kwargs)`                              | Creates a new bucket.                                                                    | `bucket = client.create_bucket('my-new-bucket')`                          |
| `bucket(bucket_name)`                                               | Returns a**Bucket**object (does not check if it exists).                           | `bucket = client.bucket('my-bucket')`                                     |
| `get_bucket(bucket_name)`                                           | Gets a bucket and checks if it exists (deprecated; prefer `client.bucket().reload()`). | `bucket = client.get_bucket('my-bucket')`                                 |
| `lookup_bucket(bucket_name)`                                        | Looks for a bucket. Returns `None` if not found, instead of throwing an error.         | `bucket = client.lookup_bucket('my-bucket')`                              |
| `list_blobs(bucket_or_name, prefix=None, delimiter=None)`           | Lists blobs (files) in a bucket. Can filter by "folder" (prefix).                        | `blobs = client.list_blobs('my-bucket', prefix='folder/')`                |
| `copy_blob(blob, source_bucket, destination_bucket, new_name=None)` | Copies a blob from one bucket to another (or same bucket).                               | `client.copy_blob(blob, source_bucket, dest_bucket, new_name='copy.txt')` |
| `delete_bucket(bucket_or_name, **kwargs)`                           | Deletes a bucket (must be empty).                                                        | `client.delete_bucket('my-empty-bucket')`                                 |
| `batch()`                                                           | Creates a batch context to send multiple requests together.                              | `with client.batch(): blob1.reload(); blob2.reload()`                     |
| `get_service_account_email(project=None)`                           | Gets the GCS service account email for the project.                                      | `email = client.get_service_account_email()`                              |

---

## ✨ Examples

### 1. List all buckets

```python
for bucket in client.list_buckets():
    print(bucket.name)
```

### 2. Create a new bucket

```python
bucket = client.create_bucket('new-bucket-name')
print(f'Bucket {bucket.name} created.')
```

### 3. List all files inside a specific folder

```python
bucket = client.bucket('my-bucket')
blobs = client.list_blobs('my-bucket', prefix='folder-name/')

for blob in blobs:
    print(blob.name)
```

### 4. Copy a file to another bucket

```python
source_bucket = client.bucket('source-bucket')
destination_bucket = client.bucket('destination-bucket')
blob = source_bucket.blob('source-folder/myfile.txt')

new_blob = client.copy_blob(blob, source_bucket, destination_bucket, new_name='destination-folder/myfile_copy.txt')
print('Blob copied.')
```

---

## 🧠 Notes

* **`bucket()`** just creates a reference, it doesn't check if the bucket actually exists.
* **`list_blobs()`** is super useful for working with "folders" (prefixes).
* Always handle exceptions properly in production code (for example, `google.api_core.exceptions.NotFound`).

---

## 📎 References

* [google-cloud-storage Client Docs](https://cloud.google.com/python/docs/reference/storage/latest/client)
* [Full API Reference](https://googleapis.dev/python/storage/latest/index.html)

.