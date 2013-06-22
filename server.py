import tornado.ioloop
import tornado.web
from register import RegisterRequestHandler

class MainRequestHandler(tornado.web.RequestHandler):
    def get(self):
    	self.write("hello")



app = tornado.web.Application([(r"/",MainRequestHandler), (r"/register", RegisterRequestHandler)])

if __name__ == "__main__":
    app.listen(80)
    tornado.ioloop.IOLoop.instance().start()