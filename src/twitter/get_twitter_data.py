from firebase import firebase
app = firebase.FirebaseApplication('https://boiling-fire-6168.firebaseio.com/', None)
result = app.get('/instagram_data', None)
print(result)