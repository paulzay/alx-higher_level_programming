#!/usr/bin/python3

"""define a function"""


def class_to_json(obj):
    """function to return dict description"""
    if isinstance(obj, (list, dict, str, int, bool)):
        return obj
