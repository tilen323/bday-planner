import webapp2

from cron.bday_notification import BdayMailSendHandler
from handlers.base import MainHandler
from handlers.bday import AddBdayHandler, BdayDetailsHandler, BdayDeleteHandler
from handlers.anniversary import AddAnniversaryHandler, AnniversaryDetailsHandler, AnniversaryDeleteHandler
from handlers.event import AddEventHandler, EventDetailsHandler, EventDeleteHandler

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/bday/add', AddBdayHandler, name="bday-add"),
    webapp2.Route('/bday/details/<bday_id:\d+>', BdayDetailsHandler, name="bday-details"),
    webapp2.Route('/bday/delete/<bday_id:\d+>', BdayDeleteHandler, name="bday-delete"),
    webapp2.Route('/anniversary/add', AddAnniversaryHandler, name="anniversary-add"),
    webapp2.Route('/anniversary/details/<anniversary_id:\d+>', AnniversaryDetailsHandler, name="anniversary-details"),
    webapp2.Route('/anniversary/delete/<anniversary_id:\d+>', AnniversaryDeleteHandler, name="anniversary-delete"),
    webapp2.Route('/event/add', AddEventHandler, name="event-add"),
    webapp2.Route('/event/details/<event_id:\d+>', EventDetailsHandler, name="event-details"),
    webapp2.Route('/event/delete/<event_id:\d+>', EventDeleteHandler, name="event-delete"),

    #Cron
    webapp2.Route("/cron/mail/bday", BdayMailSendHandler, name="cron-mail-bday"),
], debug=True)
