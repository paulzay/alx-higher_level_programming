#!/usr/bin/python3

"""class definition"""


class Node:
    """Node class defining a linkedlist"""
    def __init__(self, data, next_node=None):
        """initialize variables"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value
        if type(self.__data) is not int:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return self.__data

    @next_node.setter
    def next_node(self, value):
        self.__next_node = value
        if type(self.__next_node) is not None or isinstance(next_node) != Node:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """singly linked list"""
    def __init__(self):
        pass

    def __str__(self):
        pass

    def sorted_insert(self, value):
        pass
