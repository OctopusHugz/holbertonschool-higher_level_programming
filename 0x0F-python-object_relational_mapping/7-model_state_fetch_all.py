#!/usr/bin/python3
"""This module lists all State objects from the database hbtn_0e_6_usa"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (create_engine)
from sqlalchemy import Table
from sqlalchemy import select
from sys import argv

from sqlalchemy.sql.schema import MetaData
from model_state import Base, State, Session

Base = declarative_base()


def model_state_fetch_all():
    """This function lists all State objects from the database hbtn_0e_6_usa"""
    try:
        session = Session()
        states = session.query(State).all()
        for state in states:
            print(str(state.id) + ": " + str(state.name))
            #print(state.id, state.name)
        #conn = engine.connect()
        #meta = MetaData(engine)
        #table = meta.tables['states']
        #ss = select([table])
        #rows = conn.execute(ss)
        #for row in rows:
        #    print(row)
    except:
        pass


if __name__ == '__main__':
    model_state_fetch_all()
