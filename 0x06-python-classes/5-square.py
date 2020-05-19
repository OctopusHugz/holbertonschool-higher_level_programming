#!/usr/bin/python3
class Square():
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        i = 0
        size = self.__size
        if size == 0:
            print()
        else:
            while i < size:
                j = 0
                while j < size:
                    if j != size - 1:
                        print("#", end='')
                    j += 1
                print("#")
                i += 1
