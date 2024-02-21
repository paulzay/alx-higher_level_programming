#!/usr/bin/python3

"""class"""


class BaseGeometry:
    """base geometry"""
    def __init__(self):
        """initialize data"""
        pass

    def area(self):
        """area"""
        raise Exception("area is not implemented")
