from db import Session
from math import hypot
from post import Post
from sqlalchemy import desc


import web
import time

class PostsController:
    # list all posts
    
    timeOutFilter = "(DATE_ADD(created_at, INTERVAL time_limit second)) >= NOW()"
    
    def list(self):
        session = Session()
        posts = session.query(Post).filter(self.timeOutFilter).order_by(desc(Post.created_at)).all()
        session.close()
        return posts

    def list_in_radius(self, latitude, longitude, radius):
        session = Session()
        haversine = "(6371 * acos(cos(radians(:lat)) * cos(radians(latitude)) * cos( radians(longitude) - radians(:lon)) + sin(radians(:lat)) * sin(radians(latitude)))) <= :rad"
        posts = session.query(Post).filter(haversine).params(
            lat = latitude,
            lon = longitude,
            rad = radius
        ).filter(self.timeOutFilter).order_by(desc(Post.created_at)).all()
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
                return self.list_in_radius(latitude, longitude, radius)
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
		print "sup"
		try:
			print "yooooo"
			time_limit = int(input['time_limit'])
			print time_limit
			self.add(message, latitude, longitude, time_limit)
		except ValueError:
			return "time_limit must be an integer"
            except KeyError:
                self.add(message, latitude, longitude)
