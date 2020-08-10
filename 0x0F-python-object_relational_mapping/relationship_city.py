#!/usr/bin/python3
"""This module creates a City class"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey
from relationship_state import Base


class City(Base):
    """This is an instance of the City class"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))

    def __str__(self):
        return "\t" + str(self.id) + ": " + str(self.name)
