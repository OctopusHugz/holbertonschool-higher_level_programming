#!/usr/bin/python3
"""This module creates a City class"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey
from model_state import Base


class City(Base):
    """This is an instance of the City class"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))

    def __init__(self, name, state_id, id=None):
        self.id = id
        self.name = name
        self.state_id = state_id
