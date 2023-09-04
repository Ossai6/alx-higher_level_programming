#!/usr/bin/python3
"""
This file contains the Rectangle class
"""


class Rectangle():
    """
    A class Rectangle that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """ This method instatiates the class """
        self.__width = width
        self.__height = height

        @property
        def width(self):
            """ Returns the value ofthe width """
            return __width

        @width.setter
        def width(self, value):
            """ Sets the values of the width """
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """ Returna the value of the height """
            return __height

        @height.setter
        def height(self, value):
            """ Sets the value ofthe height """
            if type(value) is not int:
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value

        def area(self):
            """ Returns the area of the rectangle """
            return __width * __height

        def perimeter(self):
            """ Retuens the perimeter of the rectangle """
            if __width == 0 or __height == 0:
                return 0
            return ((2 * __width) + (2 * __height))
