from datetime import datetime
from db import Base
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String

import json
import web

class Post(Base):
  __tablename__ = 'post'

  id = Column(Integer, primary_key=True)
  created_at = Column(DateTime, default=datetime.utcnow())
  updated_at = Column(DateTime, onupdate=datetime.utcnow())
  message = Column(String(256), nullable=False)
  longitude = Column(Float, nullable=False)
  latitude = Column(Float, nullable=False)

  def __init__(self, message, latitude, longitude):
    self.message = message
    self.latitude = latitude
    self.longitude = longitude

  def __repr__(self):
    return json.dumps({
        "id": self.id,
        "created_at": self.created_at.isoformat(),
        "updated_at": self.updated_at.isoformat() if self.updated_at != None else '',
        "message": self.message,
        "longitude": self.longitude,
        "latitude": self.latitude
      })
