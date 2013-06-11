from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *

Base = declarative_base()

class Post(Base):
	__tablename__ = "post"

	id = Column(Integer, primary_key=True)
	longitude = Column(Float)
	latitude = Column(Float)
	content = Column(String)
	title = Column(String)
	#and some relationship to tags || rooms

	def __init__(self, title, content, longitude, latitude):
		self.title = title
		self.content = content
		self.longitude = longitude
		self.latitude = latitude

	def __repr__(self):
		return "Post {title: %s, content: %s, latitude: %f, longitude: %f}" % \
		 (self.title, self.content, self.latitude, self.longitude)



engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)