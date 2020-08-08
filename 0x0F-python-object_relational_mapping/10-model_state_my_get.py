#!/usr/bin/python3
"""This module lists the first State object from the database hbtn_0e_6_usa"""
from sys import argv
from model_state import Session, State


def model_state_my_get():
    """This function lists 1st State object from the database hbtn_0e_6_usa"""
    try:
        session = Session()
        states = session.query(State).all()
        for state in states:
            if argv[4] == state.name:
                print(state.id)
                return
        print("Not found")
    except:
        pass


if __name__ == '__main__':
    model_state_my_get()
