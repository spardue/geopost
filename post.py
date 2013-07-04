from datetime import datetime
from db import Base
from sqlalchemy import Column, DateTime, Float, Integer, String

import json
import cgi

class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    message = Column(String(256), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    time_limit = Column(Integer, nullable=False)

    def __init__(self, message, latitude, longitude,  time_limit=60):
        self.message = message
        self.latitude = latitude
        self.longitude = longitude
        self.time_limit = time_limit

    def __repr__(self):
        return json.dumps({
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "time_limit": self.time_limit,
            "message": cgi.escape(self.message), #prvents insertion of javascript on the client side
            "latitude": self.latitude,
            "longitude": self.longitude,
        })
