from handlers.base import BaseHandler
from google.appengine.api import mail

class InviteFriendEmailWorker(BaseHandler):
    def post(self):
        user_email = self.request.get("user_email")
        friend_email = self.request.get("friend_email")

        mail.send_mail(sender="prevolnik.tilen@gmail.com",
                       to=friend_email,
                       subject="Bday-Planner Invitation",
                       body="Your friend %s, has sent you an invitation to Bday-Planner app - http://bday-planner.appspot.com" % user_email)