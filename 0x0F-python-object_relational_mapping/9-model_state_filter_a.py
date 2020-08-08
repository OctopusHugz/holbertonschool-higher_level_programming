#!/usr/bin/python3
"""This module lists the first State object from the database hbtn_0e_6_usa"""
from model_state import Session, State


def model_state_filter_a():
    """This function lists 1st State object from the database hbtn_0e_6_usa"""
    try:
        session = Session()
        states = session.query(State).all()
        for state in states:
            if 'a' in state.name:
                print(str(state.id) + ": " + str(state.name))
    except:
        pass


if __name__ == '__main__':
    model_state_filter_a()
