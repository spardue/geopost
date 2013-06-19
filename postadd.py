from data import Post, Session
import web

class postadd:
	def GET(self):
		input = web.input()
		
		print(web.input())
		longitude = input["longitude"]
		latitude = input["latitude"]
		message = input["message"]

		post = Post(message, latitude, longitude)

		session = Session()
		session.add(post)

		session.commit()

		return post


