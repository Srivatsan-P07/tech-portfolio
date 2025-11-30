import firebase_admin
from firebase_admin import credentials, firestore

if not firebase_admin._apps:
    cred = credentials.Certificate('../serviceAccountKey.json')
    firebase_admin.initialize_app(cred)

db = firestore.client(database_id='hawx-brahmin-db')

col_ref = db.collection('sample_collection')

# Read
doc_ref = col_ref.document('custom_doc_id')
doc = doc_ref.get()

if doc.exists:
    print(f'Document_data: {doc.to_dict()}')
    print('-------------------------------')

# query
query_ref = col_ref.where(
    filter=firestore.FieldFilter('name', '==', 'Srivatsan')
    ).stream()
for doc in query_ref:
    print(doc.id)
    print(doc.to_dict())

# Modify

doc_ref2 = col_ref.document('lMRIxqkgSLCD3HvDglcM')
doc_ref2.update({
    'age': 29,
    'name': 'Saisaran'
})

# Delete

doc_ref3 = col_ref.document('HLqvJJxyTOZjlqmziZyt')
doc_ref3.delete()