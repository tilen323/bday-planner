from google.appengine.ext import ndb

class Bday(ndb.Model):
    title = ndb.StringProperty(default="bday")
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    avatar = ndb.StringProperty(default="https://s21.postimg.org/bu6oqrxg7/man.png")
    bday_date = ndb.DateTimeProperty()
    user_email = ndb.StringProperty()
    deleted = ndb.BooleanProperty(default=False)
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def add_bday(cls, first_name, last_name, avatar, bday_date, user_email):
        new_bday = Bday(first_name=first_name, last_name=last_name, avatar=avatar, bday_date=bday_date, user_email=user_email)
        new_bday.put()

    @classmethod
    def add_bday_no_image(cls, first_name, last_name, bday_date, user_email):
        new_bday = Bday(first_name=first_name, last_name=last_name, bday_date=bday_date, user_email=user_email)
        new_bday.put()