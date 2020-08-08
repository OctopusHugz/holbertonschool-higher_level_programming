#!/usr/bin/python3
"""This module lists the first State object from the database hbtn_0e_6_usa"""
from sys import argv
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
from model_state import Base, State


def model_state_update_id_2():
    """This function lists 1st State object from the database hbtn_0e_6_usa"""
    session = Session()
    state = session.query(State).filter(State.id == 2)
    print(state[0].name)
    state[0].name = "New Mexico"
    print(state[0].name)
    session.commit()
    session.close()


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    model_state_update_id_2()
