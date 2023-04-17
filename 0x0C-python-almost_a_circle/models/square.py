#!/usr/bin/python3
"""
This module contains the Square class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This Square class represents a square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square.
        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        prints a string representation of a Square
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """gets the size of the square"""
        return self.height

    @size.setter
    def size(self, value):
        """sets the width and height of the
        square to a value
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args:
            if len(args) >= 1:
                self.id = args[0]
            else:
                self.id
            if len(args) >= 2:
                self.size = args[1]
            else:
                self.size
            if len(args) >= 3:
                self.x = args[2]
            else:
                self.x
            if len(args) >= 4:
                self.y = args[3]
            else:
                self.y
        elif kwargs:
            if 'id' in kwargs:
                self.id = kwargs['id']
            else:
                self.id
            if 'size' in kwargs:
                self.size = kwargs['size']
            else:
                self.size
            if 'x' in kwargs:
                self.x = kwargs['x']
            else:
                self.x
            if 'y' in kwargs:
                self.y = kwargs['y']
            else:
                self.y

    def to_dictionary(self):
        return {'id': self.id, 'width': self.width, 'height': self.height, 'x': self.x, 'y': self.y}
