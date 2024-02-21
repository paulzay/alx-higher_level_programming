#!/usr/bin/python3

"""class"""


class BaseGeometry:
    """class stuff"""
    def area(self):
        """area function"""
        raise Exception("area is not implemented")

    def integer_validator(self, name, value):
        """integer validator"""
        if type(value) is not int:
            raise TypeError(name + " is not an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
