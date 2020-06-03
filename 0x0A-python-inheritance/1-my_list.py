#!/usr/bin/python3
"""This module implements a class MyList that inherits from list class"""


class MyList(list):
    """The MyList class defines a list object"""

    def print_sorted(self):
        """This module prints the MyList instance in sorted order"""
        if type(self) != list or not isinstance(self, list):
            raise TypeError("input must be a list")
        print(sorted(self))
