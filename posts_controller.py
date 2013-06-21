from db import Session
from post import Post

import web

# Post Controller
class PostsController(object):
  def GET(self, post_id):
    session = Session()
    if post_id == '':
      input = web.input()
      # TODO Check for curr_longitude and curr_latitude
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
    else:
      return web.notfound()

  def PUT(self, post_id):
    if post_id != '':
      session = Session()
      input = web.input()
      post = session.query(Post).get(post_id)
      try:
        post.message = input['message']
      except KeyError:
        pass
      try:
        post.latitude = input['latitude']
      except KeyError:
        pass
      try:
        post.longitude = input['longitude']
      except KeyError:
        pass
      session.add(post)
    else:
      return web.notfound()

  def DELETE(self, post_id):
    if post_id != '':
      session = Session()
      session.delete(session.query(Post).get(post_id))
    else:
      return web.notfound()
