#!/usr/bin/python3
"""This module implements the Base class"""
from models.base import Base


class Rectangle(Base):
    """This is the Rectangle class's instantiation"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """This function creates the Rectangle instance"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """This function overrides the __str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    @property
    def width(self):
        """This getter function returns the Rectangle's width attribute"""
        return self.__width

    @width.setter
    def width(self, width):
        """This setter function sets the Rectangle's width attribute"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """This getter function returns the Rectangle's height attribute"""
        return self.__height

    @height.setter
    def height(self, height):
        """This setter function sets the Rectangle's height attribute"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """This getter function returns the Rectangle's x attribute"""
        return self.__x

    @x.setter
    def x(self, x):
        """This setter function sets the Rectangle's x attribute"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """This getter function returns the Rectangle's y attribute"""
        return self.__y

    @y.setter
    def y(self, y):
        """This setter function sets the Rectangle's y attribute"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """This function returns the Rectangle's area"""
        return self.__width * self.__height

    def display(self):
        """This function prints the Rectangle to stdout"""
        right_shift = self.__x
        down_shift = self.__y
        for rows in range(down_shift):
            print()
        rows = 0
        for rows in range(self.__height):
            cols = 0
            print(" " * right_shift, end="")
            for cols in range(self.__width):
                print("#", end="")
                cols += 1
            print()
            rows += 1
