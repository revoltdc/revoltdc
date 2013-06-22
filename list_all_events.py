import tornado.ioloop
import tornado.web
from mock_data import user
from mock_data import events
from twilio.rest import TwilioRestClient
registered = False
class ListAllEventsHandler(tornado.web.RequestHandler):
    def get(self,*args):
        
        self.render("events.html",all_events=events)
    def post(self):
        pass
class SeeEventHandler(tornado.web.RequestHandler):
    def get(self,*args):
        global registered
        event_id=str(self.get_argument("event_id"))
        this_event="";
        for i in range(len(events)):
            if events[i]["event_id"]==event_id:
                this_event=events[i]
                break
        print registered
        self.render("event_details.html",e=this_event, reg=registered)
        print registered
    def post(self):
        global registered
        account_sid = "AC954b92ab3aa3fe23cee06ae56b384019"
        auth_token = "b037fe51ee05147c69c806d78b3d9e95"
        client = TwilioRestClient(account_sid, auth_token)
        message = client.sms.messages.create(to="7033005458", from_="7039400998", body="dkjjdlkds!")
        print registered
        registered = True
        print registered
        self.get()