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
