import tornado.ioloop
import tornado.web
from mock_data import user


class RegisterRequestHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("signup.html")
	def post(self):
		entry = {}
		entry["first"] = str(self.get_argument("firstname"))
		entry["last"] = str(self.get_argument("lastname"))
		entry["email"] = str(self.get_argument("email"))
		entry["password"] = str(self.get_argument("password"))
		entry["phone"] = str(self.get_argument("phone"))
		entry["potential"] = str(self.get_argument("political"))
		entry["zip"] = str(self.get_argument("zip"))
		user.append(entry)
		self.write(str(user))