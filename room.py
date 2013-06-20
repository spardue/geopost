from datetime import datetime
from db import Base
from post import Post
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship, backref

import json
import web


class Room(Base):
  __tablename__ = 'room'

  id = Column(Integer, primary_key=True)
  created_at = Column(DateTime, default=datetime.utcnow)
  updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
  private = Column(Boolean)
  title = Column(String(32))
  # TODO Test the relationship.
  posts = relationship('Post', backref='room', cascade_backrefs=True)

  def __init__(self, title, private):
    self.title = title
    self.private = private

  def __repr__(self):
    return json.dumps(self.__dict__)

