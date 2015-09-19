from firebase import firebase
def retrive(suffix=''):
    app = firebase.FirebaseApplication('https://boiling-fire-6168.firebaseio.com/'+suffix, None)
    return app.get('/instagram_data', None)
if __name__ == '__main__':
    #freeze_support()
    print(retrive())
