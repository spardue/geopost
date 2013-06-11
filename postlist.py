from data import Post, Session
import web

class postlist:
	def GET(self):
		session = Session()
		return list(session.query(Post).filter())