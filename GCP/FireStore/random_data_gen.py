
import firebase_admin
from firebase_admin import credentials, firestore
import random
import time
from datetime import datetime


# --- CONFIGURATION ---

# 1. Path to your Service Account Key file. 
#    Replace 'path/to/your/serviceAccountKey.json' with the actual path.
#    This file is necessary for server-side authentication with Firebase.
COLLECTION_NAME = 'random_data'
NUM_DOCUMENTS = 100

# --- DATA GENERATION HELPERS ---
NAMES = ["Alice Johnson", "Bob Smith", "Charlie Brown", "Diana Prince", "Eve Adams", 
         "Frank Miller", "Grace Lee", "Henry Kim", "Ivy Rodriguez", "Jack Wilson", 
         "Kelly Chen", "Leo Davis", "Mia Garcia", "Noah Martinez", "Olivia Hall"]
LOCATIONS = ["New York, USA", "London, UK", "Tokyo, Japan", "Paris, France", 
             "Berlin, Germany", "Sydney, Australia", "Dubai, UAE", "Singapore", 
             "Toronto, Canada", "Rio de Janeiro, Brazil", "San Francisco, USA"]

def generate_random_document(index: int) -> dict:
    """Generates a single dictionary representing a Firestore document."""
    name = random.choice(NAMES)
    age = random.randint(18, 65)
    location = random.choice(LOCATIONS)

    return {
        'name': name,
        'age': age,
        'location': location,
        'created_at': firestore.SERVER_TIMESTAMP, # Use server timestamp for accuracy
        'document_index': index + 1
    }

def upload_data_batch(db: firestore.client):
    """
    Generates 100 random documents and uploads them to Firestore 
    using a single, efficient batch write operation.
    """
    print(f"Starting batch write for {NUM_DOCUMENTS} documents...")
    start_time = time.time()

    # Get a new batch instance
    batch = db.batch()
    
    # Get a reference to the target collection
    collection_ref = db.collection(COLLECTION_NAME)

    for i in range(NUM_DOCUMENTS):
        doc_data = generate_random_document(i)
        
        # Create a new document reference with an auto-generated ID
        doc_ref = collection_ref.document() 
        
        # Add the set operation to the batch
        batch.set(doc_ref, doc_data)
        
        if (i + 1) % 10 == 0:
            print(f"    - {i + 1} documents prepared in batch...")

    try:
        # Commit the batch write (sends all operations as one atomic request)
        batch.commit()
        end_time = time.time()
        duration = end_time - start_time
        
        print("\n--- UPLOAD SUCCESS ---")
        print(f"✅ Successfully uploaded {NUM_DOCUMENTS} documents to collection '{COLLECTION_NAME}'.")
        print(f"Total time taken: {duration:.2f} seconds.")
        print(f"View your data in the Firebase Console under the '{COLLECTION_NAME}' collection.")

    except Exception as e:
        print("\n--- UPLOAD FAILED ---")
        print(f"❌ An error occurred during batch commit: {e}")
        print("Please ensure your SERVICE_ACCOUNT_KEY_PATH is correct and the key has 'Cloud Datastore User' permissions.")


# --- MAIN EXECUTION ---
if __name__ == '__main__':
    try:
        if not firebase_admin._apps:
            cred = credentials.Certificate('../serviceAccountKey.json')
            firebase_admin.initialize_app(cred)
        db = firestore.client(database_id='hawx-brahmin-db')
        
        # 3. Run the upload function
        upload_data_batch(db)

    except FileNotFoundError:
        print(f"\nFATAL ERROR: Service Account Key file not found at '{SERVICE_ACCOUNT_KEY_PATH}'.")
        print("Please update the SERVICE_ACCOUNT_KEY_PATH variable in the script.")
    except Exception as e:
        print(f"\nFATAL ERROR: Could not initialize Firebase Admin SDK. {e}")