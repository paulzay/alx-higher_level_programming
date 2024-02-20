#!/usr/bin/python3

"""function to decode json"""
import json


def from_json_string(my_str):
    """function to decode json"""
    return json.load(my_str)
