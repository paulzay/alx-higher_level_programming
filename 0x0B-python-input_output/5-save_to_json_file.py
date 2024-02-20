#!/usr/bin/python3

""" define function to save to json"""
import json


def save_to_json_file(my_obj, filename):
    """ function to save to json"""
    with open(filename, "w") as mf:
        text = json.dumps(my_obj)
        return mf.write(text)
