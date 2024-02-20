#!/usr/bin/python3

"""class definition"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """initialize data"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """function work desc"""
        if (type(attrs)) == list and all(type(i) == str for i in attrs):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """function work desc"""
        for i in json:
            self.__dict__.update({i: json[i]})
