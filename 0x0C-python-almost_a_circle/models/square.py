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
        x = self.x
        y = self.y
        width = self.width
        return "[Square] ({}) {}/{} - {}".format(self.id, x, y, width)

    @property
    def size(self):
        """This getter function returns the Square's size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """This setter function sets the Square's size attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """This function assigns a key/value argument to the Square's
attributes"""
        if args and args[0]:
            try:
                self.id = args[0]
            except Exception as e:
                pass
            try:
                self.size = args[1]
            except Exception as e:
                pass
            try:
                self.x = args[2]
            except Exception as e:
                pass
            try:
                self.y = args[3]
            except Exception as e:
                pass
        else:
            try:
                self.id = kwargs["id"]
            except Exception as e:
                pass
            try:
                self.size = kwargs["size"]
            except Exception as e:
                pass
            try:
                self.x = kwargs["x"]
            except Exception as e:
                pass
            try:
                self.y = kwargs["y"]
            except Exception as e:
                pass
