#!/usr/bin/python3

def read_file(filename=""):
    """ function to read file and print the output """
    with open(filename, mode="r", encoding="utf-8") as MYFILE:
        print(MYFILE.read(), end="")
