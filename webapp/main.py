import os
import webapp2
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

# from firebase import firebase
# Example of firebase
# firebase = firebase.FirebaseApplication('https://your_storage.firebaseio.com', None)
# result = firebase.get('/users', None)

spots_to_find = ['Food', 'Nightlife', 'Spots', 'Activities']

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
        # for spot in spots_to_find:
            # <option value="{{spot}}">{{spot}}</option>
        self.render("main_form.html")

    def post(self):
        distance = self.request.get("distance")
        find = self.request.get("find")
        lon = self.request.get("lon")
        lat = self.request.get("lat")

        # we know distance and location from
        # here we will send stuff to firebase and get the 3
        self.write('hello again. Distance: ' + distance)


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
