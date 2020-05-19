#!/usr/bin/python3
"""This module declares a Square class that initializes a private
size attribute if the size argument is verified. It then computes
the area of the Square that was instantiated using a setter function"""


class Square:
    """This Square class initializes the instance's private size attribute
after verifying it in the setter function. It then uses the getter function
to obtain that size attribute. It then uses that size to compute its area"""

    def __init__(self, size=0):
        """This function initializes an instance of the Square class and assigns
the private attribute size to the instance if size is the correct int type."""
        self.__size = size

    def area(self):
        """This function takes the size attribute of the object and uses
it to compute its area"""
        return self.__size ** 2

    @property
    def size(self):
        """This getter function gets the size attribute of the instance
and returns it"""
        return self.__size

    @size.setter
    def size(self, value):
        """This setter function validates the size argument given at instantiation.
If valid, it sets the size attribute for the instance."""
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
