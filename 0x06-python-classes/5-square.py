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
    def size(self, size):
        """ setter of size """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ calculate square area """
        return self.__size ** 2

    def my_print(self):
        """ print the square """
        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#", self.__size)
