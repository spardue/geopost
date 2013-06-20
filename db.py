from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base(bind=engine)
Session = scoped_session(sessionmaker(engine))
