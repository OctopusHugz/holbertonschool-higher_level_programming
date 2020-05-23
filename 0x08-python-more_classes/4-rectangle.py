#!/usr/bin/python3
"""This module implements a rectangle class with private height
and width attributes"""


class Rectangle:
    """This class implements private height and width attributes"""

    def __init__(self, width=0, height=0):
        """This __init__ function creates the instace with the attributes"""
        self.width = width
        self.height = height

    def __str__(self):
        """This function prints the string representation of a rectangle"""
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        rows = 0
        while rows < self.__height:
            cols = 0
            while cols < self.__width:
                string += "#"
                cols += 1
            if rows + 1 != self.__height:
                string += "\n"
            rows += 1
        return string

    def __repr__(self):
        """This function prints the string representation of a rectangle"""
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        string += "Rectangle(" + str(self.__width) + \
            ", " + str(self.__height) + ")"
        return string

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

    def area(self):
        """This method returns the rectangle's area"""
        return self.__height * self.__width

    def perimeter(self):
        """This method returns the rectangle's perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height * 2) + (self.__width * 2)
