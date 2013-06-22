import tornado.ioloop
import tornado.web
import os
from register import RegisterRequestHandler
from list_all_events import ListAllEventsHandler
from list_all_events import SeeEventHandler

def Get_Location(ipv4):
    apy_key="056a68ee3510ce527fbc9981e6860c0ba7631e8c8f489d8d841be2c196e770f7"
    format="json"
    request_url="http://api.ipinfodb.com/v3/ip-city/?key="+apy_key+"&ip="+ipv4+"&format="+format
    response=urllib.urlopen(request_url)
    return response.read()

import mock_data


class MainRequestHandler(tornado.web.RequestHandler):
    def get(self):
    	self.render("index.html")

settings = {'debug': True, 
            'static_path': os.path.join(os.getcwd(), 'static')}
static_path = os.path.join(os.getcwd(), 'static')


app = tornado.web.Application([(r"/",MainRequestHandler), 
                               (r"/register", RegisterRequestHandler), 
                               (r"/events", ListAllEventsHandler), 
                               (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": static_path}),
                               (r"/event_details", SeeEventHandler)], **settings)

if __name__ == "__main__":
	print mock_data.user
	app.listen(80)
	tornado.ioloop.IOLoop.instance().start()
