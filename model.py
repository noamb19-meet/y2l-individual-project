from sqlalchemy import Column, Integer, String, Boolean
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
