from handlers.base import BaseHandler
from utils.decorators import validate_csrf


class EventHandler(BaseHandler):
    def get(self):

        return self.render_template("event.html")