from db import Session
from post import Post

import web

class PostController(object):
  def GET(self):
    return self.list()
#    if post_id != None:
#      input = web.input()
#      curr_longitude = input['curr_longitude'] or None
#      curr_latitude = input['curr_latitude'] or None
#      if curr_longitude == None and curr_latitude == None:
#        return self.list()
#      else:
#        return self.list(curr_longitude, curr_latitude)
#    else:
#      return self.show(post_id)

  def POST(self):
    input = web.input()
    title = input['title'] or None
    content = input['content'] or None
    longitude = input['longitude'] or None
    latitude = input['latitude'] or None
    return self.create(title, content, longitude, latitude)

  def PUT(self):
    input = web.input()
    title = input['title'] or None
    content = input['content'] or None
    longitude = input['longitude'] or None
    latitude = input['latitude'] or None
#    return self.update(post_id)
    print 'not yet implemented'

  def DELETE(self):
#    return self.delete(post_id)
    print 'not yet implemented'

  # list all Posts
  def list(self, curr_longitude=None, curr_latitude=None):
    session = Session()
    post_list = list(session.query(Post))
    return repr(post_list)

  # create a new Post
  def create(self, title, content, longitude, latitude):
    post = Post(title, content, longitude, latitude)
    session = Session()
    session.add(post)
    session.commit()
    return repr(post)

  # show a Post
  def show(self, post_id):
    session = Session()
    post = session.query(Post).get(post_id)
    return repr(post)

  # update a Post
  def update(self, post_id, title=None, content=None, longitude=None, latitude=None):
    session = Session()
    post = session.query(Post).get(post_id)
    post.title = title or post.title
    post.content = content or post.content
    post.longitude = longitude or post.longitude
    post.latitude = latitude or post.latitude
    session.add(post)
    session.commit()
    return repr(post)

  # delete a Post
  def delete(self, post_id):
    session = Session()
    post = session.query(Post).get(post_id)
    session.delete(post)
    session.commit()
