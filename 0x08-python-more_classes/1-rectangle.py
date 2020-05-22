#!/usr/bin/python3
"""This module implements a rectangle class with private height
and width attributes"""


class Rectangle:
    """This class implements private height and width attributes"""

    def __init__(self, width=0, height=0):
        """This __init__ function creates the instace with the attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """This getter returns the rectangle's width"""
        return self.__width

    @width.setter
    def width(self, value):
        """This setter sets the width of the rectangle after validation"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This getter returns the rectangle's height"""
        return self.__height

    @height.setter
    def height(self, value):
        """This setter sets the height of the rectangle after validation"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
