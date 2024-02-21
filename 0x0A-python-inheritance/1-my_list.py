#!/usr/bin/python3

"""define list child class"""


class MyList(list):
    """child class that prints sorted list"""
    def __init__(self):
        """initialize data"""
        super().__init__()

    def print_sorted(self):
        """print the sorted list"""
        print(sorted(self))
