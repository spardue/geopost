from db import Session
from post import Post

import web

# Post Controller
class PostsController(object):
  def GET(self, post_id):
    input = web.input()
    session = Session()
    if post_id == '':
      return list(session.query(Post).filter())
    else:
      post = session.query(Post).get(post_id)
      return post

  def POST(self, post_id):
    if post_id == '':
      input = web.input()
      message = input['message']
      latitude = input['latitude']
      longitude = input['longitude']
      post = Post(message, latitude, longitude)
      session = Session()
      session.add(post)
      session.commit()
      return post

  def PUT(self, post_id):
    return None

  def DELETE(self, post_id):
    return None
