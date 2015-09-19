import os
import webapp2

# from firebase import firebase
# Example of firebase
# firebase = firebase.FirebaseApplication('https://your_storage.firebaseio.com', None)
# result = firebase.get('/users', None)

# handlers classes:
class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

# Example of RequestHandler
class MainPage(Handler):
    def get(self):
        self.write('Hello, World!')


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
