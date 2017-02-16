#!/usr/bin/env python
import os
import jinja2
import webapp2
from time import gmtime, strftime
from google.appengine.api import users
from google.appengine.api import urlfetch


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        user = users.get_current_user()

        logiran = False
        login_url = ""
        logout_url = ""

        if user:
            logiran = True
            user_nickname = user.nickname()

            logout_url = users.create_logout_url("/")

        else:
            user_nickname = "neznanec"
            login_url = users.create_login_url("/")

        params = {"logiran": logiran, "login_url": login_url, "logout_url": logout_url, "user_nickname": user_nickname}
        return self.render_template("hello.html", params=params)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
