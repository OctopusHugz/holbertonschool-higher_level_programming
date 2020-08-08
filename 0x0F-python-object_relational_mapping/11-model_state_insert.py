#!/usr/bin/python3
"""This module lists the first State object from the database hbtn_0e_6_usa"""
from model_state import Session, State


def model_state_insert():
    """This function lists 1st State object from the database hbtn_0e_6_usa"""
    try:
        session = Session()
        state = State(6, "Louisiana")
        print(str(state.id))
        session.add(state)
        session.commit()
        session.close()
    except:
        pass


if __name__ == '__main__':
    model_state_insert()
