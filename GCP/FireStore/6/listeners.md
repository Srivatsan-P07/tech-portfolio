## ⚡ Realtime Listeners in GCP Firestore with Python

**Realtime Listeners** in Cloud Firestore allow your application to receive automatic updates whenever data changes in the database. Instead of manually polling for changes, you establish a persistent connection that "streams" updates, enabling real-time features like live chat or collaborative documents.

### Snapshot Listeners

The core mechanism for real-time updates is the **Snapshot Listener**, implemented using the `on_snapshot()` method in the Python client library. You attach this listener to a specific **document** or **query** (collection/filtered collection).

When you attach a listener:

1.  Firestore immediately sends an initial **query snapshot** containing the current state of the documents that match your query.
2.  The connection remains open, and any subsequent changes to the matching data trigger a new snapshot.

### Python Example: Listening to a Document

This example shows how to listen to a single document using the `on_snapshot()` method.

```python
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import threading
import time

# --- Setup (Assumes you have set up credentials/initialized the app) ---
# cred = credentials.ApplicationDefault()
# firebase_admin.initialize_app(cred)
# db = firestore.client()

# Placeholder for the actual Firestore client setup
class MockFirestoreClient:
    def collection(self, collection_name):
        return self
    def document(self, document_name):
        return self
    def on_snapshot(self, callback):
        print("Listener registered.")
        # In a real app, this would return an object to unsubscribe
        # For this example, we'll return a mock object.
        class MockUnsubscriber:
            def unsubscribe(self):
                print("Listener unsubscribed.")
        return MockUnsubscriber()

db = MockFirestoreClient() 
# --- End Setup ---

# 1. Define the Callback Function
def on_document_snapshot(doc_snapshot, changes, read_time):
    """
    Callback function that is executed whenever the document changes.
    
    Args:
        doc_snapshot: The current DocumentSnapshot or QuerySnapshot.
        changes: A list of DocumentChange objects (relevant for collection queries).
        read_time: The time the snapshot was read from the database.
    """
    
    # The doc_snapshot is iterable, even for a single document reference
    for doc in doc_snapshot:
        if doc.exists:
            print(f"\n✅ Document Update Received at {read_time}:")
            print(f"   Document ID: {doc.id}")
            print(f"   Data: {doc.to_dict()}")
        else:
            print(f"\n❌ Document Removed at {read_time}: {doc.id}")
            
    # For a collection/query, you would iterate over 'changes' to see 
    # if a document was ADDED, MODIFIED, or REMOVED.
    
# 2. Attach the Snapshot Listener to a Document
# Replace 'cities' and 'SF' with your actual collection and document IDs
doc_ref = db.collection('cities').document('SF')

# This line establishes the persistent connection and runs the callback 
# on a background thread whenever data changes.
# The result is an object you can use to stop listening.
doc_watch = doc_ref.on_snapshot(on_document_snapshot)

# In a real-world scenario (like a server), your main thread needs to 
# stay alive for the listener's background thread to continue running.
# For demonstration:
print("Listening... Press Ctrl+C to stop.")
# time.sleep(60) # Keep the main thread alive for 60 seconds

# To stop listening, you call the unsubscribe method:
# doc_watch.unsubscribe()
```

-----

### Key Concepts

| Feature | Description |
| :--- | :--- |
| **Snapshot Listeners** | The general term for the real-time functionality. You attach a listener to a document (`DocumentReference.on_snapshot`) or a query (`Query.on_snapshot`). |
| **Callbacks** | A function (like `on_document_snapshot` above) that you provide to `on_snapshot()`. This function is executed every time the data changes or when the initial data is loaded. |
| **Streaming Updates** | The underlying mechanism. Firestore uses a persistent, long-lived connection to push data changes to your client immediately, rather than the client repeatedly requesting (polling) the server for updates.  |
| **Limitations** | Realtime listeners are powerful, but consider: <br>- **Billing:** Listeners consume document reads for the initial snapshot and one read for every update that is streamed to the client. Long-running listeners can be costly.<br>- **Connection Overhead:** Maintaining many concurrent long-lived connections can impact server resources.<br>- **Concurrency:** In Python, the callback runs on a separate background thread. You must be careful with thread-safe access to any shared state or global variables in your main application.<br>- **Offline Persistence (Not Python Admin SDK):** While mobile/web SDKs often handle offline updates, the Python Admin SDK is generally for server-side code and does not typically support offline persistence for listeners. |

