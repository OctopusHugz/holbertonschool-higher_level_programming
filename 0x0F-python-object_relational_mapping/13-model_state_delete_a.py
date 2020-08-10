#!/usr/bin/python3
"""This module deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa"""
from sys import argv
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
from model_state import Base, State


def model_state_delete_a():
    """This function deletes all State objects with a name containing the letter
a from the database hbtn_0e_6_usa"""
    session = Session()
    states = session.query(State).filter(State.name.like(
        '%a%')).delete(synchronize_session=False)
    session.commit()


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    model_state_delete_a()
