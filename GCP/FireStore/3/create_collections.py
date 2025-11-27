import firebase_admin
from firebase_admin import credentials, firestore

if not firebase_admin._apps:
    cred = credentials.Certificate('../serviceAccountKey.json')
    firebase_admin.initialize_app(cred)

db = firestore.client(database_id='hawx-brahmin-db')

# Create random documents

doc_ref1 = db.collection('sample_collection')

data = {
    'name': 'Srivatsan',
    'age': 26
}

update_time, doc_ref = doc_ref1.add(data)

doc_ref2 = db.collection('sample_collection').document('custom_doc_id')
data2 = {
    'name': 'John Doe',
    'age': 30
}
doc_ref2.set(data2, merge=False)  # Overwrites if exists

sub_col = doc_ref2.collection('sub_collection')
sub_col.add({'item': 'Sample Item', 'quantity': 5})
