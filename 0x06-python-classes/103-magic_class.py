#!/usr/bin/python3
""" Magic class """
import math


class MagicClass(object):
    """ magic class"""
    def __init__(self, radius=0):
        """ initialize clss """
        """args: radius=0: radius"""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicaClass__radius = radius

    def area(self):
        """ calc tha area"""
        return (self._MagicaClass__radius ** 2) * math.pi

    def circumference(self):
        """calc the circumference"""
        return (self._MagicaClass__radius * 2) * math.pi
