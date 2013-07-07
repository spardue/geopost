from datetime import datetime
from db import Base
from sqlalchemy import Column, DateTime, Float, Integer, String, TIMESTAMP, text

import json
import cgi

class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    created_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    message = Column(String(256), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    time_limit = Column(Integer, nullable=False)

    def __init__(self, message, latitude, longitude,  time_limit=60):
        self.message = cgi.escape(message) # strip html/javascript
        self.latitude = latitude
        self.longitude = longitude
        self.time_limit = time_limit

    def __repr__(self):
        return json.dumps({
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "time_limit": self.time_limit,
            "message": self.message,
            "latitude": self.latitude,
            "longitude": self.longitude,
        })
