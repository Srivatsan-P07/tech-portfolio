# 📄 GCS Python Client - Quick Cheatsheet


**Setup**

```python
from google.cloud import storage
client = storage.Client()
bucket = client.bucket('your-bucket-name')
blob = bucket.blob('path/to/file.txt')
```

---

## 🔵 Client (`storage.Client`)

| Action        | Code                                    |
| :------------ | :-------------------------------------- |
| List buckets  | `client.list_buckets()`               |
| Get bucket    | `client.get_bucket('bucket-name')`    |
| Create bucket | `client.create_bucket('bucket-name')` |
| Delete bucket | `bucket.delete()`                     |

---

## 🟡 Bucket (`storage.Bucket`)

| Action                 | Code                                                                |
| :--------------------- | :------------------------------------------------------------------ |
| List blobs             | `bucket.list_blobs()`                                             |
| Create blob reference  | `blob = bucket.blob('file.txt')`                                  |
| Get blob               | `blob = bucket.get_blob('file.txt')`                              |
| Delete blob            | `bucket.delete_blob('file.txt')`                                  |
| Delete multiple blobs  | `bucket.delete_blobs(['file1.txt', 'file2.txt'])`                 |
| Check if bucket exists | `bucket.exists()`                                                 |
| Make bucket public     | `bucket.make_public()`                                            |
| Make bucket private    | `bucket.make_private()`                                           |
| Rename blob            | `bucket.rename_blob(blob, 'newname.txt')`                         |
| Copy blob              | `bucket.copy_blob(blob, destination_bucket, new_name='copy.txt')` |
| Get IAM policy         | `bucket.get_iam_policy()`                                         |
| Set IAM policy         | `bucket.set_iam_policy(policy)`                                   |

---

## 🟣 Blob (`storage.Blob`)

| Action               | Code                                                 |
| :------------------- | :--------------------------------------------------- |
| Upload file          | `blob.upload_from_filename('local/path/file.txt')` |
| Upload string        | `blob.upload_from_string('Hello!')`                |
| Upload file object   | `blob.upload_from_file(open('file.txt', 'rb'))`    |
| Download to file     | `blob.download_to_filename('local/path/save.txt')` |
| Download as string   | `content = blob.download_as_string()`              |
| Download as text     | `text = blob.download_as_text()`                   |
| Delete blob          | `blob.delete()`                                    |
| Check if blob exists | `blob.exists()`                                    |
| Make blob public     | `blob.make_public()`                               |
| Make blob private    | `blob.make_private()`                              |
| Generate signed URL  | `blob.generate_signed_url(expiration=3600)`        |
| Copy blob            | `blob.rewrite(destination_blob)`                   |
| Change storage class | `blob.update_storage_class('COLDLINE')`            |

---

## 🧠 Pro Tips

* Use **prefix** in `list_blobs(prefix='folder/')` to list files inside a folder.
* `make_public()` on bucket/ blob gives open internet access. 🔥 (Use carefully!)
* **Signed URLs** are safe for temporary private file sharing (like presigned S3 URLs).
* Bucket must be  **empty before deletion** .

.
