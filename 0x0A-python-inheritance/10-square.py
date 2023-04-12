#!/usr/bin/python3
"""
This module contains the class BaseGeometry and subclass Rectangle
"""


"""Importing the class Rectancle from 9-rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class has two methods
    """
    def __init__(self, size):
        """instantiating the object"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns the area"""
        return self.__size * self.__size
