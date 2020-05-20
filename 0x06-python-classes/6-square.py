#!/usr/bin/python3
"""This module declares a Square class that initializes a private
size attribute if the size argument is verified. It then computes
the area of the Square that was instantiated using a setter function.
It also handles the positioning of the square."""


class Square:
    """This Square class initializes the instance's private size and position
attribute after verifying it in the setter function. It then uses the getter
function to obtain that size attribute. It then uses that size to compute
its area"""

    def __init__(self, size=0, position=(0, 0)):
        """This function initializes an instance of the Square class and assigns
the private attribute size to the instance if size is the correct int type. It
then assigns the private attribute position once it 's validated."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """This getter function gets the size attribute of the instance
and returns it"""
        return self.__size

    @size.setter
    def size(self, value):
        """This setter function validates the size argument given at instantiation.
If valid, it sets the size attribute for the instance."""
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """This getter function gets the position attribute of the instance
and returns it"""
        return self.__position

    @position.setter
    def position(self, value):
        """This setter function validates the position argument given at instantiation.
If valid, it sets the position attribute for the instance. """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not value[0] >= 0 or not value[1] >= 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """This function takes the size attribute of the object and uses
it to compute its area"""
        return self.size ** 2

    def my_print(self):
        """This function prints the square using the # character. It also prints
spaces for positioning"""
        i = 0
        size = self.size
        position = self.position
        if size == 0:
            print()
        else:
            if position[1] > 0:
                print()
            while i < size:
                j = 0
                k = 0
                while j < size:
                    while k < position[0]:
                        print(" ", end='')
                        k += 1
                    if j != size - 1:
                        print("#", end='')
                    j += 1
                print("#")
                i += 1
