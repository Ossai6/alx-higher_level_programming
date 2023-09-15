#!/usr/bin/python3
"""
This file contains the Rectangle class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ This is the Rectangle class, it inherits from BaseGoemetry class """
    def __init__(self, width, height):
        """ instantiates the Rectangle class """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
