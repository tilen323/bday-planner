from google.appengine.ext import ndb

class Bday(ndb.Model):
    title = ndb.StringProperty(default="bday")
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    date = ndb.DateTimeProperty()
    avatar = ndb.StringProperty()
    bday_year = ndb.IntegerProperty()
    bday_age = ndb.IntegerProperty()
    user_email = ndb.StringProperty()
    deleted = ndb.BooleanProperty(default=False)
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def add_bday(cls, first_name, last_name, avatar, date, bday_year, bday_age, user_email):
        new_bday = Bday(first_name=first_name, last_name=last_name, avatar=avatar, date=date, bday_age=bday_age, bday_year=bday_year, user_email=user_email)
        new_bday.put()

    @classmethod
    def delete_bday(cls,bday):
        bday.deleted = True
        bday.put()
        return bday

    @classmethod
    def edit_bday(cls, bday, first_name, last_name, avatar, date):
        bday.first_name = first_name
        bday.last_name = last_name
        bday.avatar = avatar
        bday.date = date
        bday.put()
        return bday
