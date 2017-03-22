import os
import uuid

import jinja2
import webapp2

from google.appengine.api import users, memcache
from datetime import datetime, timedelta
from operator import itemgetter, attrgetter

from models.user_profile import User
from models.bday import Bday
from models.anniversary import Anniversary
from models.event import Event

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
        user = users.get_current_user()
        if user:

            bday_list = Bday.query(Bday.user_email == user.email(),
                                   Bday.date > datetime.now(),
                                   Bday.date < datetime.now() + timedelta(days=30)).fetch()

            anniversary_list = Anniversary.query(Anniversary.user_email == user.email(),
                                                 Anniversary.date > datetime.now(),
                                                 Anniversary.date < datetime.now() + timedelta(days=30)).fetch()

            event_list = Event.query(Event.user_email == user.email(),
                                     Event.date > datetime.now(),
                                     Event.date < datetime.now() + timedelta(days=30)).fetch()

            new_list = []

            if bday_list:
                for bday in bday_list:
                    new_list.append(bday)

            if anniversary_list:
                for anniversary in anniversary_list:
                    new_list.append(anniversary)

            if event_list:
                for event in event_list:
                    new_list.append(event)

            new_sorted_list = sorted(new_list, key=attrgetter('date'))

            params = {"new_sorted_list": new_sorted_list}
        else:
            params = {"user": user}

        return self.render_template("hello.html", params=params)
















