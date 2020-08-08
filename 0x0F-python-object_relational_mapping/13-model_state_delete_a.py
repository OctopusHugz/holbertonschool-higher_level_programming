#!/usr/bin/python3
"""This module lists the first State object from the database hbtn_0e_6_usa"""
from model_state import Session, State


def model_state_delete_a():
    """This function lists 1st State object from the database hbtn_0e_6_usa"""
    try:
        session = Session()
        states = session.query(State).filter(State.name.like(
            '%a%')).delete(synchronize_session=False)
        session.commit()
        session.close()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    model_state_delete_a()
