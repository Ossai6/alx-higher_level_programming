#!/usr/bin/python3
"""
    This module contains the class Rectangle and a subclass Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        This represents a square
    """
    def __init__(self, size):
        """ instantiation of a square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ returns the area of a square"""
        return self.__size**2

    def __str__(self):
        """ returns the string representation of a square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
