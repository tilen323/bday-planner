import os
import uuid

import jinja2
import webapp2

from google.appengine.api import users, memcache

from models.user_profile import User

template_dir = os.path.join(os.path.dirname(__file__), "../templates")
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

        user = users.get_current_user()

        if user:
            params["user"] = User.get_or_create(user.email())
            params["logout_url"] = users.create_logout_url("/")

            self.response.set_cookie(key="bday-cookie", value="accepted")

        else:
            params["login_url"] = users.create_login_url("/")

        csrf_token = str(uuid.uuid4())  # convert UUID to string
        memcache.add(key=csrf_token, value=True, time=600)
        params["csrf_token"] = csrf_token

        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):

        return self.render_template("hello.html")

class BdayHandler(BaseHandler):
    def get(self):

        return self.render_template("bday.html")

class AnniversaryHandler(BaseHandler):
    def get(self):

        return self.render_template("anniversary.html")

class AddEditHandler(BaseHandler):
    def get(self):

        return self.render_template("add_edit.html")

class AboutHandler(BaseHandler):
    def get(self):

        return self.render_template("about.html")