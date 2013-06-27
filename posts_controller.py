from db import Session
from dist import earth_dist
from math import hypot
from post import Post
from sqlalchemy import desc

import web

class PostsController:
    # list all posts
    def list(self):
        session = Session()
        posts = session.query(Post).order_by(Post.created_at.asc()).all()
        session.close()
        return posts

    def list_in_radius(self, latitude, longitude, radius):
        session = Session()
        posts = session.query(Post).filter(earth_dist(Post.latitude, latitude, Post.longitude, longitude) <= radius).order_by(Post.created_at.desc()).all()
        session.close();
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
    def add(self, message, latitude, longitude, radius, time_limit=60):
        print radius
        post = Post(message, latitude, longitude, radius, time_limit)
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
                print "got key error"
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
            radius = input['radius']
            try:
                time_limit = input['time_limit']
                self.add(message, latitude, longitude, radius, time_limit)
            except KeyError:
                self.add(message, latitude, longitude, radius)
