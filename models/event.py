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
    updated = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def add_event(cls, event_name, location, avatar, event_date, user_email):
        new_event = Event(event_name=event_name, location=location, avatar=avatar, event_date=event_date, user_email=user_email)
        new_event.put()