#!/usr/bin/python3

"""class definition"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, x, y, width, height)
        self.width = size
        self.height = size
    
    def __str__(self):
        pass

