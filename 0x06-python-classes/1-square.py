#!/usr/bin/python3
"""This module declares a Square class that
initializes a private size attribute"""


class Square:
    """This Square class initializes the instance's private size attribute"""

    def __init__(self, size=0):
        """This function initializes an instance of the Square class and assigns
the private attribute size to the instance."""
        self.__size = size
