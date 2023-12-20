#!/usr/bin/python3
""" class that defines a square """


class Square(object):
    """ class that defines a square """
    def __init__(self, size=0):
        """
        initialize the class
        Args:
        size=0: default size
        """
        self.__size = size

    def area(self):
        """ calc the area """
        return self.__size ** 2

    @property
    def size(self):
        """ size property """
        return self.__size

    @size.setter
    def size(self, size):
        """ size setter """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
