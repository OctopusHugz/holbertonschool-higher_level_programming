#!/usr/bin/python3
"""This module lists all City objects from the database hbtn_0e_14_usa"""
from sys import argv
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
from model_city import City
from model_state import Base, State


def model_city_fetch_by_state():
    """This function lists all City objects from the database hbtn_0e_14_usa"""
    session = Session()
    for state, city in session.query(State, City).\
            filter(State.id == City.state_id):
        print(str(state.name) + ": (" +
              str(city.id) + ") " + str(city.name))


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    model_city_fetch_by_state()
