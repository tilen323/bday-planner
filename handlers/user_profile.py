from handlers.base import BaseHandler
from utils.decorators import validate_csrf

from google.appengine.api import mail
from google.appengine.api import users, memcache, taskqueue
from datetime import datetime


from models.user_profile import User

class UserProfileHandler(BaseHandler):
    def get(self):
        user = users.get_current_user()
        user_profile = User.query(User.email == user.email()).get()

        params = {"user_profile": user_profile}

        return self.render_template("user_profile.html", params=params)


class UserProfileEditHandler(BaseHandler):
    def get(self, user_profile_id):
        user_profile = User.get_by_id(int(user_profile_id))

        params = {"user_profile": user_profile}

        return self.render_template("user_profile_edit.html", params=params)

    @validate_csrf
    def post(self, user_profile_id):
        user_profile = User.get_by_id(int(user_profile_id))

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

        if not avatar:
            avatar = "https://s21.postimg.org/bu6oqrxg7/man.png"

        User.edit_profile(user_profile=user_profile,
                          first_name=first_name,
                          last_name=last_name,
                          bday_date=datetime_object,
                          bday_year=int(bday_year),
                          bday_age=bday_age,
                          avatar=avatar)

        return self.redirect_to("user-profile")


class InviteFriendHandler(BaseHandler):
    @validate_csrf
    def post(self):
        user = users.get_current_user()
        friend_email = self.request.get("email")

        taskqueue.add(url='/task/invite-friend', params={"user_email": user.email(),
                                                         "friend_email": friend_email})

        return self.redirect_to("user-profile")
