#!/usr/bin/python3
"""This module implements the Student class"""


class Student:
    """This is an instance of the Student class"""

    def __init__(self, first_name, last_name, age):
        """This function creates the instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This function returns a dictionary representation of the instance"""
        return self.__dict__
