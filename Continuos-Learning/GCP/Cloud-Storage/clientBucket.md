# 📦 Google Cloud Storage (GCS) - `Bucket` Object Methods Guide

This document explains all the important methods available in the **`google.cloud.storage.Bucket`** object when using the  **Google Cloud Storage Python Client** .

---

## 📚 Setup

Initialize the client and get the bucket:

```python
from google.cloud import storage

client = storage.Client()
bucket = client.bucket('your-bucket-name')
```

---

## 🛠️ `Bucket` - Main Methods

| Method                                                 | Description                                                                                                 | Example                                                             |
| :----------------------------------------------------- | :---------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------ |
| `blob(blob_name)`                                    | Creates a**Blob**object inside the bucket (does not upload).                                          | `blob = bucket.blob('path/to/file.txt')`                          |
| `list_blobs(prefix=None, delimiter=None)`            | Lists all blobs in the bucket. Optionally filter with a prefix.                                             | `blobs = bucket.list_blobs()`                                     |
| `exists()`                                           | Checks if the bucket exists in GCS.                                                                         | `bucket.exists()`                                                 |
| `delete()`                                           | Deletes the bucket (must be empty first).                                                                   | `bucket.delete()`                                                 |
| `delete_blob(blob_name)`                             | Deletes a specific blob by name.                                                                            | `bucket.delete_blob('file.txt')`                                  |
| `delete_blobs(blobs_list)`                           | Deletes multiple blobs at once.                                                                             | `bucket.delete_blobs(['file1.txt', 'file2.txt'])`                 |
| `get_blob(blob_name)`                                | Retrieves an existing blob if it exists, else `None`.                                                     | `blob = bucket.get_blob('file.txt')`                              |
| `upload_blob_from_filename(local_file, blob_name)`   | (Custom wrapper) Upload a file to a blob path.*(You normally use `blob.upload_from_filename()`though.)* | N/A                                                                 |
| `rename_blob(blob, new_name)`                        | Renames a blob inside the bucket.                                                                           | `bucket.rename_blob(blob, 'newname.txt')`                         |
| `copy_blob(blob, destination_bucket, new_name=None)` | Copies a blob into this or another bucket.                                                                  | `bucket.copy_blob(blob, destination_bucket, new_name='copy.txt')` |
| `get_iam_policy(requested_policy_version=None)`      | Get the IAM policy attached to the bucket.                                                                  | `policy = bucket.get_iam_policy()`                                |
| `set_iam_policy(policy)`                             | Set a new IAM policy for the bucket.                                                                        | `bucket.set_iam_policy(policy)`                                   |
| `make_public(future=False)`                          | Makes the bucket publicly readable.                                                                         | `bucket.make_public()`                                            |
| `make_private(future=False)`                         | Makes the bucket private (requires setting ACLs).                                                           | `bucket.make_private()`                                           |
| `reload()`                                           | Reloads the bucket's metadata from GCS.                                                                     | `bucket.reload()`                                                 |
| `patch()`                                            | Updates changes made locally (ex: changing versioning, labels).                                             | `bucket.patch()`                                                  |
| `update()`                                           | Same as patch, but used less often.                                                                         | `bucket.update()`                                                 |

---

## ✨ Examples

### 1. List all blobs (files) in the bucket

```python
blobs = bucket.list_blobs()
for blob in blobs:
    print(blob.name)
```

---

### 2. Check if the bucket exists

```python
if bucket.exists():
    print("Bucket exists!")
else:
    print("Bucket not found.")
```

---

### 3. Upload a file to a bucket

```python
blob = bucket.blob('folder/myfile.txt')
blob.upload_from_filename('local/path/to/myfile.txt')
print("File uploaded!")
```

---

### 4. Delete a file from the bucket

```python
bucket.delete_blob('folder/myfile.txt')
print("File deleted!")
```

---

### 5. Delete multiple files

```python
bucket.delete_blobs(['folder/file1.txt', 'folder/file2.txt'])
print("Multiple files deleted!")
```

---

### 6. Rename a file inside the bucket

```python
blob = bucket.blob('folder/oldname.txt')
new_blob = bucket.rename_blob(blob, 'folder/newname.txt')
print("Blob renamed!")
```

---

### 7. Copy a file to another bucket

```python
source_blob = bucket.blob('folder/myfile.txt')
destination_bucket = client.bucket('other-bucket')
bucket.copy_blob(source_blob, destination_bucket, new_name='new-folder/myfile_copy.txt')
print("Blob copied to another bucket.")
```

---

## 🧠 Notes

* **bucket.blob('path')** just  **creates a Blob reference** . It doesn’t upload anything yet.
* **bucket.list_blobs(prefix='folder/')** can be used to mimic folder structure.
* Before deleting a bucket, ensure **all blobs are deleted** or you’ll get a **409 Conflict** error.

---

## 📎 References

* [google-cloud-storage Bucket Docs](https://cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket)
* [Full API Reference](https://googleapis.dev/python/storage/latest/index.html)

.