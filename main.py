import webapp2

from handlers.base import MainHandler
from handlers.bday import  AddBdayHandler
from handlers.anniversary import AddAnniversaryHandler
from handlers.event import AddEventHandler

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/bday/add', AddBdayHandler, name="bday-add"),
    webapp2.Route('/anniversary/add', AddAnniversaryHandler, name="anniversary-add"),
    webapp2.Route('/event/add', AddEventHandler, name="event-add"),
], debug=True)
