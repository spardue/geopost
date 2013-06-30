from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

# engine = create_engine('sqlite:///geopost.db', echo=True)
engine = create_engine('mysql://geopost:post@localhost', echo=True)
engine.execute("CREATE DATABASE IF NOT EXISTS geopost")
engine.execute("USE geopost")

Base = declarative_base(bind=engine)
Session = scoped_session(sessionmaker(engine))
