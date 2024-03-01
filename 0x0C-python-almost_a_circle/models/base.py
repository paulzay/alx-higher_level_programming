#!/usr/bin/python3

"""define class"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """to json"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    # def save_to_file(cls, list_objs):
    #     """save to file"""
    #     pass

    def from_json_string(json_string):
        """from json"""
        if json_string is None:
            return "[]"
        return json.loads(json_string)

    # def create(cls, **dictionary):
    #     """create"""
    #     pass

    # def load_from_file(cls):
    #     """load from file"""
    #     pass
