#!/usr/bin/python3
"""This module implements the add_integer function"""


def add_integer(a, b=98):
    """The add_integer function verifies that parameters provided to
the function are either floats or ints. Then returns the result
of the addition. """
    if type(a) not in [float, int]:
        raise TypeError("a must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) not in [float, int]:
        raise TypeError("b must be an integer")
    if type(b) is float:
        b = int(b)
    return a + b
