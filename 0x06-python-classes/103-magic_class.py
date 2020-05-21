#!/usr/bin/python3
"""This module declares a MagicClass class that initializes a private
radius attribute if the radius argument is verified. It then computes
the area or circumference."""


class MagicClass:
    """This MagicClass class initializes the instance's private radius attribute
after verifying it. It also computers area or circumference based on radius."""

    def __init__(self, radius=0):
        self.__radius = 0
        """This function initializes an instance of the MagicClass class and assigns
the private attribute radius to the instance if radius is the correct int or
float type."""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """This function returns the calculated area based off the radius"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """This function returns the calculated circumference based off
the radius"""
        return 2 * math.pi * self.__radius
