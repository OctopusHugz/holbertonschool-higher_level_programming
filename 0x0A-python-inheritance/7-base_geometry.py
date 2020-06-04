#!/usr/bin/python3
"""This module implements the BaseGeometry class"""


class BaseGeometry:
    """This creates an instance of the BaseGeometry class"""

    def area(self):
        """This function raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This functions validates that the value provided is an integer"""
        if type(value) != int or not isinstance(value, int):
            raise TypeError("[TypeError] {} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
