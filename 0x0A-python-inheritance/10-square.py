#!/usr/bin/python3
""" This module contains the Square class """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """ instantiates the Square class """
        self.integer_validator("size", size)
        super().__init__(size, size)
