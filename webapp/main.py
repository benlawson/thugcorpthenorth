import os
import webapp2
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

# from firebase import firebase
# Example of firebase
# firebase = firebase.FirebaseApplication('https://your_storage.firebaseio.com', None)
# result = firebase.get('/users', None)


main_page = """
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

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

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
