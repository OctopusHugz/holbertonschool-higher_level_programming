#!/usr/bin/python3
"""This module lists the first State object from the database hbtn_0e_6_usa"""
from model_state import Session, State


def model_state_update_id_2():
    """This function lists 1st State object from the database hbtn_0e_6_usa"""
    try:
        session = Session()
        state = session.query(State).filter(State.id == 2)
        print(state[0].name)
        state[0].name = "New Mexico"
        print(state[0].name)
        session.commit()
        #session.close()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    model_state_update_id_2()
