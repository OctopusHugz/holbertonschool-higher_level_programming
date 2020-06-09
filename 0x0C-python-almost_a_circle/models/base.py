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

    @staticmethod
    def to_json_string(list_dictionaries):
        """This function returns the JSON string representation of
list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """This function writes the JSON string representation of list_objs
to a file"""
        filename = cls.__name__ + ".json"
        new_list = []
        with open(filename, "w") as fp:
            if list_objs is None:
                fp.write("[]")
            else:
                for objs in list_objs:
                    new_list.append(cls.to_dictionary(objs))
                fp.write(cls.to_json_string(new_list))
