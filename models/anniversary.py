from google.appengine.ext import ndb

class Anniversary(ndb.Model):
    title = ndb.StringProperty(default="anniversary")
    anniversary_name = ndb.StringProperty()
    avatar = ndb.StringProperty()
    anniversary_date = ndb.DateTimeProperty()
    user_email = ndb.StringProperty()
    deleted = ndb.BooleanProperty(default=False)
    created = ndb.DateTimeProperty(auto_now_add=True)