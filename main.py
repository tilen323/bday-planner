import webapp2
from handlers.base import MainHandler, BdayHandler, AnniversaryHandler, AddEditHandler, AboutHandler


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/bday', BdayHandler),
    webapp2.Route('/anniversary', AnniversaryHandler),
    webapp2.Route('/add_edit', AddEditHandler),
    webapp2.Route('/about', AboutHandler),
], debug=True)
