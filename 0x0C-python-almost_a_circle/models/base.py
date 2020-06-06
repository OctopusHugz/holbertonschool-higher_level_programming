#!/usr/bin/python3
"""This module implements the Base class"""
import json


class Base:
    """This is the Base class's instantiation"""
    __nb_objects = 0

    def __init__(self, id=None):
        """This function creates the Base instance"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    def to_json_string(list_dictionaries):
        """This function returns the JSON string representation of
list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
