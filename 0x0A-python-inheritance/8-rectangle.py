#!/usr/bin/python3
"""
This module cotains a subclass Rectangle
"""


"""Importing the BaseGeometry class from its module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This method defines a rectangle
    """
    def __init__(self, width, height):
        """
        instantiating the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
