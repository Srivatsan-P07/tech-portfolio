import firebase_admin
from firebase_admin import credentials, firestore

if not firebase_admin._apps:
    cred = credentials.Certificate('../serviceAccountKey.json')
    firebase_admin.initialize_app(cred)

db = firestore.client(database_id='hawx-brahmin-db')

# Full Stream
col_ref = db.collection('random_data')
docs = col_ref.limit(5).stream()

for doc in docs:
    print(f"{doc.id} => {doc.to_dict()}")

print("--------------------------------------------------")
# Filter Stream
query = (
    col_ref
    .where(filter = firestore.FieldFilter('age', '<', 35))
    .where(filter = firestore.FieldFilter('location', 'in', ['New York, USA']))
    .limit(5)
)

docs = query.stream()
for doc in docs:
    print(f" {doc.id} => {doc.to_dict()}    ")

print("--------------------------------------------------")
# Order By
query = (
    col_ref
    .order_by(field_path = 'age', direction = firestore.Query.ASCENDING)
    .limit(5)
)

docs = query.stream()
for doc in docs:
    print(f" {doc.id} => {doc.to_dict()}    ")

