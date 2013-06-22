import tornado.ioloop
import tornado.web

class MainRequestHandler(tornado.web.RequestHandler):
    def get(self):
    	self.write("hello")


app = tornado.web.Application([(r"/app",MainRequestHandler)])

if __name__ == "__main__":
    app.listen(80)
   	tornado.ioloop.IOLoop.instance().start()
