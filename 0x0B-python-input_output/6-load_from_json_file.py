#!/usr/bin/python3

"""define function to read from json"""
import json


def load_from_json_file(filename):
    """function to read from json file"""
    with open(filename, "r") as mf:
        return json.load(mf)
