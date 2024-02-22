#!/usr/bin/python3

"""square class definition"""


class Square:
    """ square class"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize data"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        self.__size = value

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """position getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter"""
        self.__position = value
        if type(position) is not tuple or len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """area of square"""
        return self.__size * self.__size

    def my_print(self):
        """print square with #"""
        if self.__size == 0:
            print()
            return

        for y in range(0, self.__position[1]):
            print()

        for i in range(0, self.__size):
            for x in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()
