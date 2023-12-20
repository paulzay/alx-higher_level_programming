#!/usr/bin/python3
"""
class that defines a squaare
"""


class Square(object):
    """
    class that defines a squaare
    """
    def __init__(self, size=0):
        """
        initialize the class
        Args: size=0: default value of size
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
