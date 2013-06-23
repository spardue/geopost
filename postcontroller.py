import web
from db import Session
from post import Post

class PostController:

	def POST(self):
		input = web.input()

		longitude = input["longitude"]
		latitude = input["latitude"]
		message = input["message"]
		try:
			limit = input["limit"]
			post = Post(message, latitude, longitude, limit)
		except KeyError:
			post = Post(message, latitude, longitude)

		session = Session()
		session.add(post)

		session.commit()

		return post

	def GET(self):
		input = web.input()
		session = Session()
		try: # if given ID
			id  = input["id"]
			return str(session.query(Post).get(id))
		except KeyError: 
			try: # haven't tested this yet
				longitude = input["longitude"]
				latitude = input["latitude"]
				radius = input["radius"]
				posts = session.query(Post).select(
					((Post.longitude - longitude)**2 + (Post.latitude - latitude)**2) <= radius**2
				)
				return list(posts)
				
			except KeyError: #if not given id, just list everything
				return list(reversed(list(session.query(Post).filter())))