#!/usr/bin/python3
"""This module lists all State objects from the database hbtn_0e_6_usa"""
from model_state import Base, State, engine, Session
import sqlalchemy


def model_state_fetch_all():
    """This function lists all State objects from the database hbtn_0e_6_usa"""
    states = Session().query(State).all()
    for state in states:
        print(state)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    model_state_fetch_all()
