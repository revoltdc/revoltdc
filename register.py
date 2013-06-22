import tornado.ioloop
import tornado.web

class RegisterRequestHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("signup.html")
	def post(self):
		self.write(self.get_argument("firstname"))