from google.appengine.ext import ndb

class User(ndb.Model):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    bday_date = ndb.DateTimeProperty()
    email = ndb.StringProperty()
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