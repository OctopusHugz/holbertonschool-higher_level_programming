#!/usr/bin/python3
class Square():
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        print("Size getter method called")
        return self.__size

    @size.setter
    def size(self, value):
        print("Setter method called")
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        print("position getter method called")
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple):
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
                else:
                    raise TypeError(
                        "position must be a tuple of 2 positive integers")
            else:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        i = 0
        size = self.__size
        position = self.__position
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
