#!/usr/bin/python3

"""class definition"""

Rectangle = __import__('8-rectangle').Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size):
        """initialzie data"""
        self.__size = size
        self.integer_validator("size", size)

        super().__init__(size, size)

    def area(self):
        """calc area of square"""
        return self.__size * self.__size
