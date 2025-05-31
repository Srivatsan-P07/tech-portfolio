# 📦 Google Cloud Storage (GCS) - `Blob` Object Methods Guide

This document covers all the important methods available in the **`google.cloud.storage.Blob`** class, part of the  **GCS Python Client** .

---

## 📚 Setup

First initialize the client, bucket, and blob:

```python
from google.cloud import storage

client = storage.Client()
bucket = client.bucket('your-bucket-name')
blob = bucket.blob('path/to/your/file.txt')
```

---

## 🛠️ `Blob` - Main Methods

| Method                                          | Description                                           | Example                                                 |
| :---------------------------------------------- | :---------------------------------------------------- | :------------------------------------------------------ |
| `upload_from_filename(filename)`              | Uploads a local file to the blob.                     | `blob.upload_from_filename('local/path/to/file.txt')` |
| `upload_from_string(data, content_type=None)` | Uploads a string or bytes to the blob.                | `blob.upload_from_string('Hello, world!')`            |
| `upload_from_file(file_obj)`                  | Uploads from a file-like object (streaming upload).   | `blob.upload_from_file(open('file.txt', 'rb'))`       |
| `download_to_filename(filename)`              | Downloads blob contents to a local file.              | `blob.download_to_filename('local/path/to/save.txt')` |
| `download_as_string()`                        | Downloads blob contents into memory as bytes.         | `content = blob.download_as_string()`                 |
| `download_as_text(encoding='utf-8')`          | Downloads blob contents into memory as text.          | `text = blob.download_as_text()`                      |
| `exists()`                                    | Checks if the blob exists.                            | `blob.exists()`                                       |
| `delete()`                                    | Deletes the blob.                                     | `blob.delete()`                                       |
| `reload()`                                    | Reloads metadata for the blob from GCS.               | `blob.reload()`                                       |
| `make_public()`                               | Makes the blob publicly accessible.                   | `blob.make_public()`                                  |
| `make_private()`                              | Makes the blob private again.                         | `blob.make_private()`                                 |
| `generate_signed_url(expiration, **kwargs)`   | Generates a signed URL for secure direct access.      | `url = blob.generate_signed_url(expiration=3600)`     |
| `rewrite(destination_blob)`                   | Copies the blob to another blob, even across buckets. | `blob.rewrite(destination_blob)`                      |
| `update_storage_class(storage_class)`         | Changes storage class (e.g., to "COLDLINE").          | `blob.update_storage_class('COLDLINE')`               |
| `patch()`                                     | Updates partial changes to blob metadata.             | `blob.patch()`                                        |

---

## ✨ Examples

### 1. Upload a local file to GCS

```python
blob = bucket.blob('folder/myfile.txt')
blob.upload_from_filename('local/path/to/myfile.txt')
print("File uploaded!")
```

---

### 2. Upload a text string directly

```python
blob = bucket.blob('folder/greeting.txt')
blob.upload_from_string('Hello, Google Cloud!')
print("String uploaded!")
```

---

### 3. Download a file from GCS to local

```python
blob = bucket.blob('folder/myfile.txt')
blob.download_to_filename('local/path/to/savefile.txt')
print("File downloaded!")
```

---

### 4. Download content into memory

```python
blob = bucket.blob('folder/myfile.txt')
content = blob.download_as_text()
print(content)
```

---

### 5. Check if a blob exists

```python
if blob.exists():
    print("Blob exists!")
else:
    print("Blob does not exist.")
```

---

### 6. Delete a blob

```python
blob.delete()
print("Blob deleted!")
```

---

### 7. Make a blob publicly accessible

```python
blob.make_public()
print("Blob public URL:", blob.public_url)
```

---

### 8. Generate a signed URL (private access for limited time)

```python
from datetime import timedelta

url = blob.generate_signed_url(expiration=timedelta(minutes=15))
print(f"Signed URL (valid 15 min): {url}")
```

---

### 9. Copy blob to another bucket

```python
destination_bucket = client.bucket('destination-bucket-name')
destination_blob = destination_bucket.blob('new-folder/copied-file.txt')
blob.rewrite(destination_blob)
print("Blob copied.")
```

---

## 🧠 Notes

* `upload_from_string` is super useful for small dynamic data (like JSON or logs).
* Signed URLs are **must-have** for temporary secure file sharing.
* You can control  **content types** ,  **metadata** ,  **cache control** , and **encryption keys** while uploading files.

---

## 📎 References

* [google-cloud-storage Blob Docs](https://cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob)
* [Full API Reference](https://googleapis.dev/python/storage/latest/index.html)

.