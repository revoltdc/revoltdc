import tornado.ioloop
import tornado.web
from register import RegisterRequestHandler
import mock_data

class MainRequestHandler(tornado.web.RequestHandler):
    def get(self):
    	self.render("index.html")



app = tornado.web.Application([(r"/",MainRequestHandler), (r"/register", RegisterRequestHandler)])

if __name__ == "__main__":
	print mock_data.user
	app.listen(80)
	tornado.ioloop.IOLoop.instance().start()