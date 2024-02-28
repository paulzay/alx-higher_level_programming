#!/usr/bin/python3

"""class definition"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize data"""
        super().__init__(size, size, x, y, id)

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
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.height)

    def update(self, *args, **kwargs):
        """update function"""
        if args and len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for j in kwargs:
                if j == "id":
                    self.id = kwargs[j]
                if j == "size":
                    self.size = kwargs[j]
                if j == "x":
                    self.x = kwargs[j]
                if j == "y":
                    self.y = kwargs[j]

    def to_dictionary(self):
        """dixt"""
        return {
                "id": self.id, "size": self.width,
                "x": self.x, "y": self.y
            }
