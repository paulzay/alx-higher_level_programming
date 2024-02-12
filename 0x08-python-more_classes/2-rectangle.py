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
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ width property """
        return self.__width

    @property
    def height(self):
        """ height property """
        return self.__height

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ area of rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ perimeter of rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)
