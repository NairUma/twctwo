import webapp2
import jinja2
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

#map_pick will set-up which map will be used by returning the url
#map0 will be a blank map that reads "ERROR, START AND END POINT CANNOT BE THE SAME"
#map 00 will be a blank map that reads "LOCATION ERROR"
# # this the home page, using /home
class MainPage(webapp2.RequestHandler):
    def get(self):
        main_template = the_jinja_env.get_template('templates/index.html')
        self.response.headers['Content-Type'] = 'html'
        self.response.write(main_template.render())

    def post(self):
        pass

# # this the map page, using /fastestpath
class FastPage(webapp2.RequestHandler):
    def get(self):
        end_template = the_jinja_env.get_template('templates/map.html')
        # adding request.get *********************************

        start_choice = self.request.get('start')
        dest_choice = self.request.get('dest')
        map_url = map_pick(start_choice, dest_choice)
        timer = timer_pick(start_choice, dest_choice)
        the_variable_dict = {
            "start": start_choice,
            "dest": dest_choice,
            "img_url": map_url,
            "timer_": timer
        }
        self.response.write(end_template.render(the_variable_dict))

    def post(self):
        # results_template = the_jinja_env.get_template('templates/map.html')
        # location_one = self.request.get('starting point')
        # location_two = self.request.get('destination')
        # map_url = map_pick(location_one, location_two)
        # the_variable_dict = {
        #     "img_url": "map_url"
        # }
        # self.response.write(results_template.render(the_variable_dict))
        pass

class MapPage(webapp2.RequestHandler):
    def get(self):
        map_template = the_jinja_env.get_template('templates/map1.html')
        self.response.headers['Content-Type'] = 'html'
        the_variable_dict = {
            "img_url": "/css/images/MAPS/rawmap.png"
        }
        self.response.write(map_template.render())

class AboutPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/about.html')
        self.response.headers['Content-Type'] = 'html'
        self.response.write(about_template.render())


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/fastestpath', FastPage),
    ('/map', MapPage),
    ('/about', AboutPage)
], debug=True)
