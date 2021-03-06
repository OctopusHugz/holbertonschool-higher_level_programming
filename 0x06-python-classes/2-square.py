#!/usr/bin/python3
"""This module declares a Square class that initializes a private
size attribute if the size argument is verified"""


class Square:
    """This Square class initializes the instance's private size attribute
after verifying it"""

    def __init__(self, size=0):
        """This function initializes an instance of the Square class and assigns
the private attribute size to the instance if size is the correct int type."""
        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
