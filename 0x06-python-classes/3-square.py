#!/usr/bin/python3
"""
class defining a square
"""
class Square(object):
    def __init__(self, size=0):
        """
        initialize class 
        Args: size=0: default value of size
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self__size = size

    def area(self):
        """Calculate area of square"""
        return self.__size ** 2

