from sqlalchemy.orm import sessionmaker
from data import Post, engine
import web

class postadd:
	def GET(self):
		input = web.input()
		
		title = input["title"]
		longitude = input["longitude"]
		latitude = input["latitude"]
		content = input["content"]

		post = Post(title, content, latitude, longitude)

		Session = sessionmaker(bind=engine)

		session = Session()
		session.add(post)

		session.commit()

		return "sup bitches"


