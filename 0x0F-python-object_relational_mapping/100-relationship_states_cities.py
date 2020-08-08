#!/usr/bin/python3
"""This module lists the first State object from the database hbtn_0e_6_usa"""
from relationship_city import City
from sys import argv
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
from model_state import Base, State


def model_state_insert():
    """This function lists 1st State object from the database hbtn_0e_6_usa"""
    session = Session()
    state = State("California")
    session.add(state)
    session.commit()
    city = City("San Francisco", state.id)
    session.add(city)
    session.commit()
    session.close()


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    model_state_insert()
