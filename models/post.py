from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
import web
import json
import datetime

class Post(object):
  __tablename__ = 'post'

  id = Column(Integer, primary_key=True)
  created_at = Column(DateTime, default=datetime.utcnow)
  title = Column(String(32))
  content = Column(String(256))
  longitude = Column(Integer)
  latitude = Column(Integer)
  room_id = Column(Integer, ForeignKey('room.id'))

  def __init__(self, title, content, longitude, latitude, room_id):
    self.title = title
    self.content = content
    self.longitude = longitude
    self.latitude = latitude
    self.room_id = room_id

  def __repr__(self):
    return json.dumps(self.__dict__)

