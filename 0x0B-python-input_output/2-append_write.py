#!/usr/bin/python3

"""define function to append string to file"""


def append_write(filename="", text=""):
    """function to append string at the end"""
    with open(filename, "a") as mf:
        return mf.write(text)
