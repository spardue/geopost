from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from datetime import datetime


engine = create_engine('sqlite:///panda.db', echo=True)
Base = declarative_base(bind=engine)

class Post(Base):
	__tablename__ = "post"

	id = Column(Integer, primary_key=True)
	longitude = Column(Float)
	latitude = Column(Float)
	message = Column(String)
	time = Column(DateTime)
	#and some relationship to tags || rooms

	def __init__(self, message, longitude, latitude):
		self.message = message
		self.longitude = longitude
		self.latitude = latitude
		self.time = datetime.now()
		
	def __repr__(self):
		return "{message: %s, latitude: %f, longitude: %f, id : %d, time : %s}" % \
		 (self.message, self.latitude, self.longitude, self.id, self.time)

Base.metadata.create_all()
Session = scoped_session(sessionmaker(engine))