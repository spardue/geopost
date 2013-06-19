from sqlalchemy import Column, Integer, String, DateTime
import web
import json

class Post(object):
  __tablename__ = 'posts'

  id = Column(Integer, primary_key=True)
  createdAt = Column(DateTime)
  title = Column(String(32))
  content = Column(String(256))
  longitude = Column(Integer)
  latitude = Column(Integer)

  def __init__(self, title, content, longitude, latitude):
    self.createdAt = datetime.now
    self.title = title
    self.content = content
    self.longitude = longitude
    self.latitude = latitude

  def __repr__(self):
    return json.dumps(self.__dict__)

