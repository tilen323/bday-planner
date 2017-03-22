from google.appengine.ext import ndb

class Event(ndb.Model):
    title = ndb.StringProperty(default="event")
    event_name = ndb.StringProperty()
    location = ndb.StringProperty()
    date = ndb.DateTimeProperty()
    avatar = ndb.StringProperty()
    user_email = ndb.StringProperty()
    deleted = ndb.BooleanProperty(default=False)
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def add_event(cls, event_name, location, avatar, date, user_email):
        new_event = Event(event_name=event_name, location=location, avatar=avatar, date=date, user_email=user_email)
        new_event.put()

    @classmethod
    def delete_event(cls, event):
        event.deleted = True
        event.put()
        return event

    @classmethod
    def edit_event(cls, event, event_name, location, avatar, date,):
        event.event_name = event_name
        event.location = location
        event.avatar = avatar
        event.date = date
        event.put()
        return event