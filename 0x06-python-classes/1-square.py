#!/usr/bin/python3
"""
Defines a class Square
"""


class Square:
    """ A class named Square
    Attributes:
        __size(int): The size of a side of the square
    """
    def __init__(self, size):
        """This method initializes a square
        Args:
            size(int): The size of a side of the square
        Returns: None.
        """
        self.__size = size
