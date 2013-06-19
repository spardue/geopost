from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship, backref
import web
import json
import datetime

from post import Post

class Room(object):
  __tablename__ = 'room'

  id = Column(Integer, primary_key=True)
  created_at = Column(DateTime, default=datetime.utcnow)
  private = Column(Boolean)
  title = Column(String(32))
  posts = relationship('Post', backref='room')

  def __init__(self, title, private):
    self.title = title
    self.private = private

  def __repr__(self):
    return json.dumps(self.__dict__)

