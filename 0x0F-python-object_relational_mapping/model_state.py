#!/usr/bin/python3
"""This module creates a State class"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """This is an instance of the State class"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    def __init__(self, name, id=None):
        self.id = id
        self.name = name
