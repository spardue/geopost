from data import Post, Session
import web

class postget:
	def GET(url, id):
		session = Session()
		return session.query(Post).get(id)