from datetime import datetime
from db import Base
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String

import json
import web

class Post(Base):
  __tablename__ = 'post'

  id = Column(Integer, primary_key=True)
  created_at = Column(DateTime, default=datetime.utcnow())
  updated_at = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())
  message = Column(String(256))
  longitude = Column(Float)
  latitude = Column(Float)

  def __init__(self, message, latitude, longitude):
    self.message = message
    self.latitude = latitude
    self.longitude = longitude

  def __repr__(self):
    return json.dumps(self.__dict__)
