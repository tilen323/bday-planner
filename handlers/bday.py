from handlers.base import BaseHandler
from utils.decorators import validate_csrf

from google.appengine.api import users
from datetime import datetime

from models.bday import Bday
from models.user_profile import User


class AddBdayHandler(BaseHandler):
    def get(self):
        return self.render_template("add_bday.html")

    @validate_csrf
    def post(self):
        user = users.get_current_user()
        user_profile = User.query(User.email == user.email()).get()
        first_name = self.request.get("first_name")
        last_name = self.request.get("last_name")
        avatar = self.request.get("avatar")

        bday_day = self.request.get("bday_day")
        bday_month = self.request.get("bday_month")
        bday_year = self.request.get("bday_year")

        bday_date = bday_day + bday_month + bday_year

        datetime_object = datetime.strptime(bday_date, '%d%m%Y')

        if avatar:
            Bday.add_bday(first_name=first_name, last_name=last_name, avatar=avatar, bday_date=datetime_object, user_email=user_profile.email)
        else:
            avatar_url = "https://s21.postimg.org/bu6oqrxg7/man.png"
            Bday.add_bday(first_name=first_name, last_name=last_name, avatar=avatar_url, bday_date=datetime_object, user_email=user_profile.email)

        return self.render_template("add_bday.html")

