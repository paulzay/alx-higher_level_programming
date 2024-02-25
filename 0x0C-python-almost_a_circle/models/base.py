#!/usr/bin/python3

"""define class"""


class Base:
    """base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        """initialize"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = base.__nb_objects

