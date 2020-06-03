#!/usr/bin/python3
"""This module implements the inherits_from function"""


def inherits_from(obj, a_class):
    """This function tests whether a given object is an instance of
a class that inherited from the given class"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
