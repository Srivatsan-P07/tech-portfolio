import firebase_admin
from firebase_admin import credentials, firestore

if not firebase_admin._apps:
    cred = credentials.Certificate('../serviceAccountKey.json')
    firebase_admin.initialize_app(cred)

db = firestore.client(database_id='hawx-brahmin-db')

# Full Stream
col_ref = (
    db.collection('random_data')
    .order_by(field_path = 'age', direction = firestore.Query.ASCENDING)
    .order_by(field_path = 'name', direction = firestore.Query.ASCENDING)
)

first_page_docs = list(col_ref.limit(5).stream())

for doc in first_page_docs:
    print(f"{doc.id} => Age: {doc.get('age')}, Name: {doc.get('name')}")

print("--------------------------------------------------")

# Pagination - Get Next Page
last_doc = None
if first_page_docs:
    last_doc = first_page_docs[-1]

    next_page_query = (
        col_ref
        .start_after(last_doc)
        .limit(5)
    )

    next_page = next_page_query.stream()
    for doc in next_page:
        print(f"{doc.id} => Age: {doc.get('age')}, Name: {doc.get('name')}")

print("--------------------------------------------------")