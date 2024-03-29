#!/usr/bin/python3

"""define rectangle"""

from models.base import Base


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

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get x"""
        return self.__x

    @property
    def y(self):
        """get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @x.setter
    def x(self, value):
        """set x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    def area(self):
        """calculate area"""
        return self.__height * self.__width

    def display(self):
        """display with #"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for i in range(self.__y)]

        for j in range(self.__height):
            [print(" ", end="") for kx in range(self.__x)]
            [print("#", end="") for lwidth in range(self.__width)]
            print("")

    def __str__(self):
        """representation"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".\
            format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """update function"""
        if args and len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            for j in kwargs:
                if j == "id":
                    self.id = kwargs[j]
                if j == "height":
                    self.__height = kwargs[j]
                if j == "width":
                    self.__width = kwargs[j]
                if j == "x":
                    self.__x = kwargs[j]
                if j == "y":
                    self.__y = kwargs[j]

    def to_dictionary(self):
        """to dict"""
        return {
                "id": self.id, "width": self.__width,
                "height": self.__height,
                "x": self.__x, "y": self.__y
            }
