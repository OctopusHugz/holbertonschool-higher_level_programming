#!/usr/bin/python3
"""This module implements the Base class"""


class Base:
    """This is the Base class's instantiation"""
    __nb_objects = 0

    def __init__(self, id=None):
        """This function creates the instance"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
