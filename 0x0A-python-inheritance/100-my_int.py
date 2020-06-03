#!/usr/bin/python3
"""This module implements the MyInt class"""


class MyInt(int):
    """This is an instance of the MyInt class"""

    def __ne__(self, other):
        """This function sets the != logic to the == logic"""
        if self == other:
            return True
        else:
            return False
