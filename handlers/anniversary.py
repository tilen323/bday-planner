from handlers.base import BaseHandler
from utils.decorators import validate_csrf

from google.appengine.api import users
from datetime import datetime

from models.user_profile import User
from models.anniversary import Anniversary


class AddAnniversaryHandler(BaseHandler):
    def get(self):
        user = users.get_current_user()
        anniversary_list = Anniversary.query(Anniversary.deleted == False,
                                             Anniversary.user_email == user.email()).order(Anniversary.date).fetch()

        params = {"anniversary_list": anniversary_list}

        return self.render_template("add_anniversary.html", params=params)

    @validate_csrf
    def post(self):
        user = users.get_current_user()
        user_profile = User.query(User.email == user.email()).get()

        anniversary_name = self.request.get("anniversary_name")
        avatar = self.request.get("avatar")

        anniversary_day = self.request.get("anniversary_day")
        anniversary_month = self.request.get("anniversary_month")
        anniversary_year = self.request.get("anniversary_year")

        now = datetime.now()

        anniversary_date = anniversary_day + anniversary_month + str(now.year)
        datetime_object = datetime.strptime(anniversary_date, '%d%m%Y')

        anniversary_age = int(now.year) - int(anniversary_year) - 1
        if now > datetime_object:
            anniversary_age = int(now.year) - int(anniversary_year)

        if now > datetime_object:
            str_datetime_object = datetime.strftime(datetime_object.date(), '%d%m%Y')
            year = int(str_datetime_object[-4:]) + 1
            anniversary_date_new = anniversary_day + anniversary_month + str(year)
            datetime_object = datetime.strptime(anniversary_date_new, '%d%m%Y')

        Anniversary.add_anniversary(anniversary_name=anniversary_name,
                                    date=datetime_object,
                                    anniversary_year=int(anniversary_year),
                                    anniversary_age=int(anniversary_age),
                                    user_email=user_profile.email,
                                    avatar=avatar)

        return self.render_template("add_anniversary.html")


class AnniversaryDetailsHandler(BaseHandler):
    def get(self, anniversary_id):
        anniversary = Anniversary.get_by_id(int(anniversary_id))

        params = {"anniversary": anniversary}
        return self.render_template("anniversary_details.html", params=params)


class AnniversaryDeleteHandler(BaseHandler):
    @validate_csrf
    def post(self, anniversary_id):
        anniversary = Anniversary.get_by_id(int(anniversary_id))
        user = users.get_current_user()

        if user.email() == anniversary.user_email:
            Anniversary.delete_anniversary(anniversary=anniversary)

        return self.redirect_to("anniversary-add")