#!/usr/bin/python3
""" This module contains the Square class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This represents the Square class that
    inherits from Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ initializes the square class """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ returns a string representation of the square """
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x,
                                             self.y, self.width)

    @property
    def size(self):
        """ gets the size of the square """
        return self.width

    @size.setter
    def size(self, value):
        """ sets the size of the square """
        self.width = value
        self.height = value
