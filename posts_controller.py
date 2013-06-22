from db import Session
from post import Post

import web

# Post Controller
class PostsController(object):

  def GET(self, post_id=None):
    session = Session()
    if post_id == None:
      input = web.input()
      try:
        curr_latitude = input['curr_latitude']
        curr_longitude = input['curr_longitude']
        distance = input['distance']
        # TODO Find posts within 'distance' to ('curr_latitude', 'curr_longitude')
        return list(session.query(Post).filter())
      except KeyError:
        return list(session.query(Post).filter())
    else:
      post = session.query(Post).get(post_id)
      if post == None:
        return web.notfound()
      return post

  def POST(self, post_id=None):
    if post_id != None:
      return web.notfound()
    input = web.input()
    message = input['message']
    latitude = input['latitude']
    longitude = input['longitude']
    post = Post(message, latitude, longitude)
    session = Session()
    session.add(post)
    session.commit()

  def PUT(self, post_id=None):
    if post_id == None:
      return web.notfound()
    session = Session()
    input = web.input()
    post = session.query(Post).get(post_id)
    if post == None:
      return self.POST(post_id)
    try:
      post.message = input['message']
      post.latitude = input['latitude']
      post.longitude = input['longitude']
    except KeyError:
      web.notfound()
    session.update(post)

  def DELETE(self, post_id=None):
    if post_id == None:
      return web.notfound()
    session = Session()
    session.delete(session.query(Post).get(post_id))
