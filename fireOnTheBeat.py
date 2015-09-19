from firebase import firebase
firebase = firebase.FirebaseApplication('https://boiling-fire-6168.firebaseio.com/', None)

new_user = 'Ozgur Vatansever'
result = firebase.post('/users', new_user)
print result
