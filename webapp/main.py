import os
import webapp2
import jinja2

# from firebase import firebase
# Example of firebase
# firebase = firebase.FirebaseApplication('https://your_storage.firebaseio.com', None)
# result = firebase.get('/users', None)

main_form = """
<form action="/map" method="post" id="mainform">
  <h2>How far away?</h2>
  <select name="Distance" form="mainform">
    <option value="1">1 mile</option>
    <option value="2">2 mile</option>
    <option value="3">3 mile</option>
    <option value="4">4 mile</option>
  </select>
  <div><textarea name="content" rows="3" cols="60"></textarea></div>
  <div><input type="submit" value="Sign Guestbook"></div>
</form>

"""

main_page =
"""
<html>
<body>
%s
</body>
</html>
"""


# handlers classes:
class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

# Example of RequestHandler
class MainPage(Handler):
    def get(self):
        output = main_page % main_form
        self.write(output)

class MapPage(Handler):
    def get(self):
        output = map_page
        self.write(output)


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
