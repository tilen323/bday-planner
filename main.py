import webapp2

from handlers.anniversary import AnniversaryHandler
from handlers.base import MainHandler
from handlers.bday import BdayHandler
from handlers.event import EventHandler

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/bday', BdayHandler, name="bday"),
    webapp2.Route('/anniversary', AnniversaryHandler, name="anniversary"),
    webapp2.Route('/event', EventHandler, name="event"),
], debug=True)
