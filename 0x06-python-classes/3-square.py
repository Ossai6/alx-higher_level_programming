#!/usr/bin/python3
"""
Defines a class Square
"""


class Square:
    """ A class named Square
    Attributes:
        __size(int): The size of a side of the square
    """
    def __init__(self, size=0):
        """This method initializes a square
        Args:
            size(int = 0): The size of a side of the square
        Returns: None.
        """
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """This method computea the area of a square
        Args:
            self: The object
        Returns: The area of a square
        """
        return (self.__size * self.__size)
