#!/usr/bin/python3
"""This module declares a Square class that initializes a private
size attribute if the size argument is verified. It then computes
the area of the Square that was instantiated using a setter function"""


class Square:
    """This Square class initializes the instance's private size attribute
after verifying it in the setter function. It then uses the getter function
to obtain that size attribute. It then uses that size to compute its area"""

    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
