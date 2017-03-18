from handlers.base import BaseHandler


class AnniversaryHandler(BaseHandler):
    def get(self):

        return self.render_template("anniversary.html")