#!/usr/bin/python3
"""This module implements the Rectangle class"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """This implements a Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """This function creates an instance of the Rectangle class"""
        try:
            self.integer_validator("width", width)
            self.__width = width
        except Exception as e:
            print(e)

        try:
            self.integer_validator("height", height)
            self.__height = height
        except Exception as e:
            print(e)

    def __str__(self):
        """This function returns a string representation of a Rectangle
instance"""
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))

    def area(self):
        """This function returns the area of the Rectangle instance"""
        return self.__width * self.__height
