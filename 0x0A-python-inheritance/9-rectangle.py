#!/usr/bin/python3

"""class definition"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ rectangle class"""
    def __init__(self, width, height):
        """initialize data"""
        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """return area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """print the rectangle dimensions"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
