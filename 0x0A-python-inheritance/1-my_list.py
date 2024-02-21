#!/usr/bin/python3

"""define list child class"""


class MyList(list):
    """child class that prints sorted list"""
    def __init__(self):
        """initialize data"""
        list.__init__(self)

    def print_sorted(self):
        """print the sorted list"""
        print(sorted(self))
