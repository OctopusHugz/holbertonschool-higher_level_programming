#!/usr/bin/python3
"""This module lists the first State object from the database hbtn_0e_6_usa"""
from relationship_city import City
from relationship_state import State
from sys import argv
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
from relationship_state import Base


def model_state_insert():
    """This function lists 1st State object from the database hbtn_0e_6_usa"""
    session = Session()
    rows = session.query(State, City).filter(
        State.id == City.state_id).order_by(State.id, City.id).all()
    count = 0
    for row in rows:
        sid1 = rows[count][0].id
        if count < len(rows) - 1:
            sid2 = rows[count - 1][0].id
            if sid1 != sid2:
                print("{:d}: {}".format(row[0].id, row[0].name))
        print("\t{:d}: {}".format(row[1].id, row[1].name))
        count += 1
    session.commit()
    session.close()


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    model_state_insert()
