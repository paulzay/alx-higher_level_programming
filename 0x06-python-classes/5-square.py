#!/usr/bin/python3
""" class that defines a square """


class Square(object):
    """ class that defines a square """
    def __init__(self, size=0):
        """ initialize class
        Args: size=0: default size value
        """
        self.__size = size

    @property
    def size(self):
        """The size property."""
        return self.__size

    @size.setter
    def size(self, value):
        """ setter of size """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ calculate square area """
        return self.__size ** 2

    def my_print(self):
        """ print the square """
        if self.__size == 0:
            print()

        for i in range(self.__size):
            [print("#", end='') for j in range(self.__size)]
            print()
