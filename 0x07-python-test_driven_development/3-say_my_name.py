#!/usr/bin/python3
"""This module implements the say_my_name function"""


def say_my_name(first_name, last_name=""):
    """The say_my_name function verifies that parameters provided to
the function are strings. Then prints a statement using those names."""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
