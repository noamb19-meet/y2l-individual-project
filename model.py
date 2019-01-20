from sqlalchemy import Column, Integer, String, Boolean,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__="User"
    id=Column(Integer, primary_key = True)
    username=Column(String)
    password=Column(String)
    family=Column(String)
    color=Column(String)

class Event (Base):
    __tablename__="Event"
    id=Column(Integer, primary_key = True)
    date=Column(DateTime)
    family=Column(String)
    name=Column(String)

