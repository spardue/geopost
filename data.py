from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


engine = create_engine('sqlite:///panda.db', echo=True)
Base = declarative_base(bind=engine)

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
		return "{title: %s, content: %s, latitude: %f, longitude: %f, id : %d}" % \
		 (self.title, self.content, self.latitude, self.longitude, self.id)

Base.metadata.create_all()
Session = scoped_session(sessionmaker(engine))