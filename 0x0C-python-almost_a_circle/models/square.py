#!/usr/bin/python3
"""This module implements the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This is the Square class's instantiation"""

    def __init__(self, size, x=0, y=0, id=None):
        """This function creates the Square instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """This function overrides the __str__ method"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
