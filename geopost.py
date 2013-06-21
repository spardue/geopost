import web
from posts_controller import PostsController
from db import Base

urls = (
  '/posts/([0-9]*)', 'PostsController'
)

app = web.application(urls, globals())

if __name__ == '__main__':
  Base.metadata.create_all()
  app.run()
