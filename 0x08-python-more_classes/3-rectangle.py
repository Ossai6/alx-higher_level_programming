#!/usr/bin/python3

from rectangle import Rectangle
""" hhhhhhhhhhhhhhhhhhhh"""


class Rectangle:
    """dddddddddddddddd"""
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        print(("#" * self.__width + "\n") * self.__height)
