from db import Base
from postcontroller import PostController

import web

routes = (
	'/post', 'PostController',
	'/', 'UiGiver',
)

class UiGiver:
	def GET(self):
		return web.redirect("/static/ui.html")

app = web.application(routes, globals())

if __name__ == '__main__':
  Base.metadata.create_all()
  app.run()
