import tornado.ioloop
import tornado.web
from mock_data import user
from mock_data import events
class ListAllEventsHandler(tornado.web.RequestHandler):
    def get(self,*args):
        
        self.render("events.html",all_events=events)
    def post(self):
        pass
    