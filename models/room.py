from sqlalchemy import Column, Integer, String, DateTime, Boolean
import web
import json

class Room(object):
  __tablename__ = 'rooms'

  id = Column(Integer, primary_key=True)
  createdAt = Column(DateTime)
  private = Column(Boolean)
  title = Column(String(32))

  def __init__(self, title, private):
    self.createdAt = datetime.now
    self.title = title
    self.private = private

  def __repr__(self):
    return json.dumps(self.__dict__)

