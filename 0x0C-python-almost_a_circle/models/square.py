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

    def update(self, *args, **kwargs):
        """
        This function assigns attributes:

        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute
        """
        if args:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id = args[0]
                self.size = args[1]
            elif len(args) == 3:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
            elif len(args) == 4:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
