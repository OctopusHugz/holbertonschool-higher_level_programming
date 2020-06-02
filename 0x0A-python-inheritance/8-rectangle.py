#!/usr/bin/python3
"""This module implements the Rectangle class"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """This implements a Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """This function creates an instance of the Rectangle class"""
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
