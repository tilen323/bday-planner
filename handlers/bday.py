from handlers.base import BaseHandler
from utils.decorators import validate_csrf

from google.appengine.api import users
from datetime import datetime

from models.bday import Bday
from models.user_profile import User


class AddBdayHandler(BaseHandler):
    def get(self):
        user = users.get_current_user()
        bday_list = Bday.query(Bday.deleted == False, Bday.user_email == user.email()).order(Bday.date).fetch()

        params = {"bday_list": bday_list}

        return self.render_template("add_bday.html", params=params)

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

        now = datetime.now()

        bday_date = bday_day + bday_month + str(now.year)

        datetime_object = datetime.strptime(bday_date, '%d%m%Y')

        bday_age = int(now.year) - int(bday_year) - 1
        if now > datetime_object:
            bday_age = int(now.year) - int(bday_year)

        if now > datetime_object:
            str_datetime_object = datetime.strftime(datetime_object.date(), '%d%m%Y')
            year = int(str_datetime_object[-4:]) + 1
            bday_date_new = bday_day + bday_month + str(year)
            datetime_object = datetime.strptime(bday_date_new, '%d%m%Y')

        if avatar:
            Bday.add_bday(first_name=first_name, last_name=last_name, avatar=avatar, date=datetime_object, bday_age=bday_age, bday_year=int(bday_year), user_email=user_profile.email)
        else:
            avatar_url = "https://s21.postimg.org/bu6oqrxg7/man.png"
            Bday.add_bday(first_name=first_name, last_name=last_name, avatar=avatar_url, date=datetime_object, bday_age=bday_age, bday_year=int(bday_year), user_email=user_profile.email)

        return self.render_template("add_bday.html")


class BdayDetailsHandler(BaseHandler):
    def get(self, bday_id):
        bday = Bday.get_by_id(int(bday_id))

        params = {"bday": bday}

        return self.render_template("bday_details.html", params=params)


class BdayDeleteHandler(BaseHandler):
    @validate_csrf
    def post(self, bday_id):
        bday = Bday.get_by_id(int(bday_id))
        user = users.get_current_user()

        if user.email() == bday.user_email:
            Bday.delete_bday(bday=bday)

        return self.redirect_to("bday-add")