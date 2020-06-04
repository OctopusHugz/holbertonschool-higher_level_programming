#!/usr/bin/python3
"""This module implements the Rectangle class"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """This implements a Square class that inherits from Rectangle"""

    def __init__(self, size):
        """This function creates an instance of the Square class"""
        try:
            self.integer_validator("size", size)
            self.__size = size
        except Exception as e:
            print(e)

    def __str__(self):
        """This function returns a string representation of a Square
instance"""
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))

    def area(self):
        """This function returns the area of the Square instance"""
        return self.__size ** 2
