#!/usr/bin/python3
"""
This module contains the square class that inherits from Rectangle cass"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class represents a square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Instantiation of the square class
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        returns the size of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        sets the width and height of the square to the same value
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        This method assigns attributes:

        *args is the list of arguments - no-keyworded arguments
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute
        """
        if args and len(args) != 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """
        returns a string representation of an object
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

    def to_dictionary(self):
        """
        returns a dictionary representation of a square object
        """
        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
        }
