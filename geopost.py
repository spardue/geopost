from db import Base
from posts_controller import PostsController

import web

routes = (
  '/posts', 'PostsController',
  '/posts/([0-9]+)', 'PostsController'
)

app = web.application(routes, globals())

if __name__ == '__main__':
  Base.metadata.create_all()
  app.run()
