#!/usr/bin/python3
"""This module implements the MyInt class"""


class MyInt(int):
    """This is an instance of the MyInt class"""

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        """This function sets the == logic to the != logic"""
        return self.value != other

    def __ne__(self, other):
        """This function sets the != logic to the == logic"""
        return self.value == other
