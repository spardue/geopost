from datetime import datetime
from db import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

import json
import web

class Post(Base):
  __tablename__ = 'post'

  id = Column(Integer, primary_key=True)
  created_at = Column(DateTime, default=datetime.utcnow())
  updated_at = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())
  content = Column(String(256))
  longitude = Column(Integer)
  latitude = Column(Integer)
#  room_id = Column(Integer, ForeignKey('room.id'))

#  def __init__(self, title, content, longitude, latitude, room_id):
  def __init__(self, title, content, latitude, longitude):
    self.title = title
    self.content = content
    self.latitude = latitude
    self.longitude = longitude
#    self.room_id = room_id

  def __repr__(self):
    return json.dumps(self.__dict__)
