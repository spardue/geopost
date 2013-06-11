from data import Post, Session
import web

class postadd:
	def GET(self):
		input = web.input()
		
		print(web.input())
		title = input["title"]
		longitude = input["longitude"]
		latitude = input["latitude"]
		content = input["content"]

		post = Post(title, content, latitude, longitude)

		session = Session()
		session.add(post)

		session.commit()

		return post


