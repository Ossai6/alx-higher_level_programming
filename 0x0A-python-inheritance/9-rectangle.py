#!/usr/bin/python3
""" This file contains the class Rectangle """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This is the Rectangle class, it inherits from
    BaseGoemetry class
    """
    def __init__(self, width, height):
        """ instantiates the Rectangle class """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ returns the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ returns a string representation of the rectangle """
        return (f"[Rectangle] {self.__width}/{self.__height}")
