from datetime import datetime, timedelta

from handlers.base import BaseHandler
from models.bday import Bday
from models.anniversary import Anniversary
from models.event import Event

from google.appengine.api import mail


class BdayMailSendHandler(BaseHandler):
    def get(self):
        bday_list = Bday.query(Bday.deleted == False,
                               Bday.date < datetime.now()).fetch()

        anniversary_list = Anniversary.query(Anniversary.deleted == False,
                                             Anniversary.date < datetime.now()).fetch()

        event_list = Event.query(Event.deleted == False,
                                 Event.date > datetime.now() + timedelta(days=1)).fetch()

        if bday_list:
            for bday in bday_list:
                mail.send_mail(sender="prevolnik.tilen@gmail.com",
                               to=bday.user_email,
                               subject="Birthday reminder",
                               body="{0} {1} has birthday today!".format(bday.first_name, bday.last_name))

                Bday.plus_one_year(bday=bday)

        if anniversary_list:
            for anniversary in anniversary_list:
                mail.send_mail(sender="prevolnik.tilen@gmail.com",
                               to=anniversary.user_email,
                               subject="Anniversary reminder",
                               body="Anniversary of {} is today!".format(anniversary.anniversary_name))

                Anniversary.plus_one_year(anniversary=anniversary)

        if event_list:
            for event in event_list:
                mail.send_mail(sender="prevolnik.tilen@gmail.com",
                               to=event.user_email,
                               subject="Event reminder",
                               body="You have {} planned in the next 24 hours!".format(event.event_name))

