#!/usr/bin/python3
"""This module lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa"""
from relationship_city import City
from relationship_state import State
from sys import argv
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
from relationship_state import Base


def relationship_states_cities_list():
    """This function lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa"""
    session = Session()
    rows = session.query(State).all()
    for state in rows:
        print(state)
        for city in state.cities:
            print("\t{:d}: {}".format(city.id, city.name))


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    relationship_states_cities_list()
