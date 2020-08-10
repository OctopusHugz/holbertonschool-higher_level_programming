#!/usr/bin/python3
"""This module creates a State class"""
from sys import argv
from sqlalchemy import Column, Integer, String
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker


Base = declarative_base()
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    argv[1], argv[2], argv[3]), pool_pre_ping=True, echo=True)
Session = sessionmaker(bind=engine)


class State(Base):
    """This is an instance of the State class"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def __str__(self):
        return str(self.id) + ": " + str(self.name)
