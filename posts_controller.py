from db import Session
from dist import earth_dist
from math import hypot
from post import Post

import web

class PostsController:
  # list all posts
  def list(self, latitude=None, longitude=None, radius=None):
    session = Session()
    if latitude != None and longitude != None and radius != None:
      posts = session.query(Post).filter(earth_dist(Post.latitude, latitude, Post.longitude, longitude) <= radius).all()
    else:
      posts = session.query(Post).all()
    session.close()
    return posts

  # show a single post
  def show(self, post_id):
    session = Session()
    post = session.query(Post).get(post_id)
    session.close()
    if post == None:
      raise web.notfound()
    else:
      return post

  # add a new post
  def add(self, message, latitude, longitude, time_limit=60):
    post = Post(message, latitude, longitude, time_limit)
    session = Session()
    session.add(post)
    session.commit()
    session.close()
    return post

  # GET /posts
  # GET /posts/<id>
  def GET(self, post_id=None):
    if post_id == None:
      input = web.input()
      try:
        latitude = input['latitude']
        longitude = input['longitude']
        radius = input['radius']
        return self.list(latitude, longitude, radius)
      except KeyError:
        return self.list()
    else:
      return self.show(post_id)

  # POST /posts
  def POST(self, post_id=None):
    if post_id != None:
      raise web.notfound()
    else:
      input = web.input()
      message = input['message']
      latitude = input['latitude']
      longitude = input['longitude']
      try:
        time_limit = input['time_limit']
        self.add(message, latitude, longitude, time_limit)
      except KeyError:
        self.add(message, latitude, longitude)
