import tornado.ioloop
import tornado.web
from mock_data import user
class ListAllEventsHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("events.html")
    def post(self):
        pass