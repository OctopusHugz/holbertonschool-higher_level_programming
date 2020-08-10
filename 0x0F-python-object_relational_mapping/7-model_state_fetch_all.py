#!/usr/bin/python3
"""This module lists all State objects from the database hbtn_0e_6_usa"""
from sys import argv
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
from model_state import Base, State


def model_state_fetch_all():
    """This function lists all State objects from the database hbtn_0e_6_usa"""
    states = Session().query(State).all()
    for state in states:
        print(state)

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    model_state_fetch_all()
