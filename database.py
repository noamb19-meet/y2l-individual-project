from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cats.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_user(username,password,family):
    print("you are signed up")
    user= User(username=username,password=password,family=family)
    session.add(user)
    session.commit()

def get_all_users():
    users=session.query(User).all()
    return users

def login(their_name,their_password):
    user = session.query(User).filter_by(username=their_name).first()
    if user!=None and str(user.password)==their_password:
        print("True")
        return user
    else:
        print("False")
        return False

def add_event(name,date,family):
    event= Event(name=name, date=date,family=family)
    session.add(event)
    session.commit()

def get_events_by_family(their_family):
    events=session.query(Event).filter_by(family=their_family).all()
    return events

