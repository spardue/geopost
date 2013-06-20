import web
from post_controller import PostController
from db import Base

urls = (
  '/posts', 'PostController'
)

app = web.application(urls, globals())

if __name__ == '__main__':
  Base.metadata.create_all()
  app.run()
