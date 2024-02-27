#!/usr/bin/python3

"""class definition"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize data"""
        super().__init__(size, size, id, x, y)

    @property
    def size(self):
        """get size"""
        return self.height

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value
    
    def __str__(self):
        """print"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.height)
