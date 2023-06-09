#!/usr/bin/python3
"""
    This module contains the class BaseGeometry and subclass
    Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        This class represents a rectangle
    """
    def __init__(self, width, height):
        """ instantiatin of the recangle"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
