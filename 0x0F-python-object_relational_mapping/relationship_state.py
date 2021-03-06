#!/usr/bin/python3
"""This module creates a State class"""
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """This is an instance of the State class"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")

    def __str__(self):
        return str(self.id) + ": " + str(self.name)
