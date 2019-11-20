import webapp2
import jinja2
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# # this the home page, using /home
class MainPage(webapp2.RequestHandler):
    def get(self):
        main_template = the_jinja_env.get_template('templates/index.html')
        self.response.headers['Content-Type'] = 'html'
        self.response.write(main_template.render())

    def post(self):
        pass

class ColePage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/cole.html')
        self.response.headers['Content-Type'] = 'html'
        self.response.write(about_template.render())

class CharliePage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/charlie.html')
        self.response.headers['Content-Type'] = 'html'
        self.response.write(about_template.render())

class LivPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/liv.html')
        self.response.headers['Content-Type'] = 'html'
        self.response.write(about_template.render())

class AspenPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/aspen.html')
        self.response.headers['Content-Type'] = 'html'
        self.response.write(about_template.render())

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/liv', LivPage),
    ('/cole', ColePage),
    ('/charlie', CharliePage),
    ('/aspen', AspenPage)
], debug=True)
