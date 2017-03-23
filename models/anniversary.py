from google.appengine.ext import ndb

class Anniversary(ndb.Model):
    title = ndb.StringProperty(default="anniversary")
    anniversary_name = ndb.StringProperty()
    avatar = ndb.StringProperty()
    date = ndb.DateTimeProperty()
    anniversary_year = ndb.IntegerProperty()
    anniversary_age = ndb.IntegerProperty()
    user_email = ndb.StringProperty()
    deleted = ndb.BooleanProperty(default=False)
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def add_anniversary(cls, anniversary_name, date, anniversary_year, anniversary_age, user_email, avatar):
        new_anniversary = Anniversary(anniversary_name=anniversary_name,
                                      date=date,
                                      anniversary_year=anniversary_year,
                                      anniversary_age=anniversary_age,
                                      user_email=user_email,
                                      avatar=avatar)
        new_anniversary.put()
        return new_anniversary

    @classmethod
    def delete_anniversary(cls, anniversary):
        anniversary.deleted = True
        anniversary.put()

        return anniversary

    @classmethod
    def edit_anniversary(cls, anniversary, anniversary_name, date, avatar):
        anniversary.anniversary_name = anniversary_name
        anniversary.date = date
        anniversary.avatar = avatar
        anniversary.put()
        return anniversary

