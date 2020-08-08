#!/usr/bin/python3
"""This module lists all State objects from the database hbtn_0e_6_usa"""
from sys import argv
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
from model_city import City
from model_state import Base, State

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    argv[1], argv[2], argv[3]), pool_pre_ping=True)
Session = sessionmaker(bind=engine)


def model_city_fetch_by_state():
    """This function lists all State objects from the database hbtn_0e_6_usa"""
    try:
        session = Session()
        for state, city in session.query(State, City).\
                filter(State.id == City.state_id):
            print(str(state.name) + ": (" +
                  str(city.id) + ") " + str(city.name))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    model_city_fetch_by_state()
