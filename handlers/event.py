from handlers.base import BaseHandler
from utils.decorators import validate_csrf

from google.appengine.api import users
from datetime import datetime

from models.user_profile import User
from models.event import Event


class AddEventHandler(BaseHandler):
    def get(self):
        user = users.get_current_user()
        event_list = Event.query(Event.deleted == False, Event.user_email == user.email()).order(Event.date).fetch()

        params = {"event_list": event_list}
        return self.render_template("add_event.html", params=params)

    @validate_csrf
    def post(self):
        user = users.get_current_user()
        user_profile = User.query(User.email == user.email()).get()

        event_name = self.request.get("event_name")
        location = self.request.get("location")
        avatar = self.request.get("avatar")

        event_day = self.request.get("event_day")
        event_month = self.request.get("event_month")
        event_year = self.request.get("event_year")
        event_hour = self.request.get("event_hour")
        event_minute = self.request.get("event_minute")

        event_date = event_day + event_month + event_year + event_hour + event_minute
        datetime_object = datetime.strptime(event_date, '%d%m%Y%H%M')

        Event.add_event(event_name=event_name, location=location, avatar=avatar, date=datetime_object, user_email=user_profile.email)

        return self.redirect_to("event-add")


class EventDetailsHandler(BaseHandler):
    def get(self, event_id):
        event = Event.get_by_id(int(event_id))

        params = {"event": event}
        return self.render_template("event_details.html", params=params)

class EventDeleteHandler(BaseHandler):
    @validate_csrf
    def post(self, event_id):
        event = Event.get_by_id(int(event_id))
        user = users.get_current_user()

        if user.email() == event.user_email:
            Event.delete_event(event=event)

        return self.redirect_to("event-add")