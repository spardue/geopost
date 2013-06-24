from datetime import datetime
from db import Base
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String

import json
import web

class Post(Base):
  __tablename__ = 'post'

  id = Column(Integer, primary_key=True)
  created_at = Column(DateTime, default=datetime.utcnow())
  time_limit = Column(Integer, nullable=False)
  message = Column(String(256), nullable=False)
  longitude = Column(Float, nullable=False)
  latitude = Column(Float, nullable=False)

  def __init__(self, message, latitude, longitude, time_limit=60):
    self.message = message
    self.latitude = latitude
    self.longitude = longitude
    self.time_limit = time_limit

  def __repr__(self):
    return json.dumps({
        "id": self.id,
        "time_limit" : self.time_limit,
        "message": self.message,
        "longitude": self.longitude,
        "latitude": self.latitude
      })
