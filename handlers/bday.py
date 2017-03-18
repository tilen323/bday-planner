from handlers.base import BaseHandler
from utils.decorators import validate_csrf


class BdayHandler(BaseHandler):
    def get(self):

        return self.render_template("bday.html")