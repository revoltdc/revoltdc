import tornado.ioloop
import tornado.web

class RegisterRequestHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("register page")
	def post(self):
		self.write("registered")