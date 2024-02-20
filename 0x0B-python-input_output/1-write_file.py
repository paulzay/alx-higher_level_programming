#!/usr/bin/python3

""" define function to write a file"""


def write_file(filename="", text=""):
    """ define function to write string to a file """
    with open(filename, "w", encoding="utf-8") as mf:
        return mf.write(text) 
