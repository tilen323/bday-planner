from google.appengine.ext import ndb

class User(ndb.Model):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    bday_date = ndb.DateTimeProperty()
    bday_year = ndb.IntegerProperty()
    bday_age = ndb.IntegerProperty()
    email = ndb.StringProperty()
    avatar = ndb.StringProperty(default="https://s21.postimg.org/bu6oqrxg7/man.png")
    deleted = ndb.BooleanProperty(default=False)
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def get_or_create(cls, email):
        user = User.query(User.email == email).get()

        if not user:
            user = User(email=email)
            user.put()

        return user

    @classmethod
    def edit_profile(cls, user_profile, first_name, last_name, bday_date, bday_year, bday_age, avatar):
        user_profile.first_name = first_name
        user_profile.last_name = last_name
        user_profile.bday_date = bday_date
        user_profile.bday_year = bday_year
        user_profile.bday_age = bday_age
        user_profile.avatar = avatar
        user_profile.put()
        return user_profile