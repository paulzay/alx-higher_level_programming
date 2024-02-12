#!/usr/bin/python3
"""
class defining a rectangle
"""


class Rectangle:
    """
    class defining a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        initialize variables
        Args arguments
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    def width(self, value):
        return self.__width

    def height(self, value):
        return self.__height
