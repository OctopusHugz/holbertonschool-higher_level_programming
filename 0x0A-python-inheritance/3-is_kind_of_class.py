#!/usr/bin/python3
"""This module implements the is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """This function tests whether a given object is an instance of,
or an instance that inherited from, the given class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
