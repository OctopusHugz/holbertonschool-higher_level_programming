#!/usr/bin/python3
"""This module creates a LockedClass instance that only allows a first_name
attribute"""


class LockedClass:
    """This class creates an instance of LockedClass"""
    __slots__ = ["first_name"]

    def __init__(self):
        """This function creates the LockedClass instance"""
        self.first_name = ""
