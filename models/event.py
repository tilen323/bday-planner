from google.appengine.ext import ndb

class Event(ndb.Model):
    title = ndb.StringProperty(default="event")
    event_name = ndb.StringProperty()
    location = ndb.StringProperty()
    avatar = ndb.StringProperty()
    event_date = ndb.DateTimeProperty()
    user_email = ndb.StringProperty()
    deleted = ndb.BooleanProperty(default=False)
    created = ndb.DateTimeProperty(auto_now_add=True)