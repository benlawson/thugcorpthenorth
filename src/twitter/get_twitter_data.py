from pprint import pprint
from firebase import firebase
firebase = firebase.FirebaseApplication('https://boiling-fire-6168.firebaseio.com/', None)
result = firebase.get('/data', None)
pprint(result)