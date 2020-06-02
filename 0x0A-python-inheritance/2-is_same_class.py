#!/usr/bin/python3
"""This module implements the is_same_class function"""


def is_same_class(obj, a_class):
    """This function tests whether a given object is exactly an
instance of the given class"""
    if type(obj) is a_class:
        return True
    else:
        return False
