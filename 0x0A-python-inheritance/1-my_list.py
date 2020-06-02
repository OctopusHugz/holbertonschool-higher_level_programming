#!/usr/bin/python3
"""This module implements a class MyList that inherits from list class"""


class MyList(list):
    """The MyList class defines a list object"""

    def print_sorted(self):
        """This module prints the MyList instance in sorted order"""
        print(sorted(self))
