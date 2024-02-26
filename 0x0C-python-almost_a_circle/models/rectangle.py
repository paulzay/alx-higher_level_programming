#!/usr/bin/python3
from models.base import Base

""" define rectangle"""


class Rectangle(Base):
    """rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize class values"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """get width"""
        return self.__width

    @property
    def height(self):
        """get height"""
        return self.__height

    @property
    def x(self):
        """get x"""
        return self.__x

    @property
    def y(self):
        """get y"""
        return self.__y

    @height.setter
    def height(self, value):
        """set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @y.setter
    def y(self, value):
        """set y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    @x.setter
    def x(self, value):
        """set x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    def area(self):
        """calculate area"""
        return self.__height * self.__width

    def display(self):
        """display with #"""
        if self.__width != 0 and self.__height != 0:
            return ""
        s = ""
        for _ in range(self.__height):
            s += "#" * self.__width + "\n"
        return s.rstrip()

    def __str__(self):
        """representation"""
        return "[Rectangle] {:d}/{:d} - {:d}/{:d} \
            ".format(self.__x, sself.__y, self.__width, self.__height)
