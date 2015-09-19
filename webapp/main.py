import os
import webapp2
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

# from firebase import firebase
# Example of firebase
# firebase = firebase.FirebaseApplication('https://your_storage.firebaseio.com', None)
# result = firebase.get('/users', None)


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
        self.render("main_form.html")

    def post(self):
        distance = self.request.get("distance")

        # we know distance and location from
        # here we will send stuff to firebase and get the 3
        self.write('hello again. Distance: ' + distance)


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
