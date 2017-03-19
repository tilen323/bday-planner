from google.appengine.ext import ndb

class Anniversary(ndb.Model):
    title = ndb.StringProperty(default="anniversary")
    anniversary_name = ndb.StringProperty()
    avatar = ndb.StringProperty()
    anniversary_date = ndb.DateTimeProperty()
    user_email = ndb.StringProperty()
    deleted = ndb.BooleanProperty(default=False)
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def add_anniversary(cls, anniversary_name, anniversary_date, user_email, avatar):
        new_anniversary = Anniversary(anniversary_name=anniversary_name,
                                      anniversary_date=anniversary_date,
                                      user_email=user_email,
                                      avatar=avatar)
        new_anniversary.put()