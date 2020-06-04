#!/usr/bin/python3
"""This module implements the Student class"""


class Student:
    """This is an instance of the Student class"""

    def __init__(self, first_name, last_name, age):
        """This function creates the instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This function returns a dictionary representation of the instance"""
        strings_list = []
        new_dict = {}
        if attrs:
            if type(attrs) is list:
                for strings in attrs:
                    if strings in self.__dict__.keys():
                        strings_list.append(strings)
                new_dict = new_dict.fromkeys(strings_list)
                for attributes in new_dict.keys():
                    value = getattr(self, attributes)
                    new_dict[attributes] = value
                return new_dict
            else:
                return self.__dict__
        else:
            return self.__dict__
