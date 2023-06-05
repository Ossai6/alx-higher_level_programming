#!/usr/bin/python3
"""
This module contains the class Rectangle
"""


class Rectangle():
    """This class represents a rectangle"""
    def __init__(self, width=0, height=0):
        """initializes the rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets and return the width to a new value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets and return the width to a new value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self. __height = value
