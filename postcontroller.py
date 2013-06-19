import web
from data import Post, Session

class PostController:
	
	def POST(self):
		input = web.input()
		
		longitude = input["longitude"]
		latitude = input["latitude"]
		message = input["message"]

		post = Post(message, latitude, longitude)

		session = Session()
		session.add(post)

		session.commit()

		return post
		
	def GET(self):
		input = web.input()
		session = Session()
		try:
			id  = input["id"]
			return str(session.query(Post).get(id))
		except KeyError:
			return list(session.query(Post).filter())