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
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        pass

    def save_to_file(cls, list_objs):
        pass

    def from_json_string(json_string):
        pass

    def create(cls, **dictionary):
        pass

    def load_from_file(cls):
        pass
