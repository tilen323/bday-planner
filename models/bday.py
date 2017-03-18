from google.appengine.ext import ndb

class Bday(ndb.Model):
    title = ndb.StringProperty(default="bday")
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    avatar = ndb.StringProperty()
    bday_date = ndb.DateTimeProperty()
    user_email = ndb.StringProperty()
    deleted = ndb.BooleanProperty(default=False)
    created = ndb.DateTimeProperty(auto_now_add=True)