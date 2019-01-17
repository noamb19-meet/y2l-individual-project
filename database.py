from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cats.db')
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

# Example of addting a student:
def login(their_name,their_password):
    user = session.query(User).filter_by(username=their_name).first()
    if user!=None and str(user.password)==their_password:
        print("True")
        return user
    else:
        print("False")
        return False
