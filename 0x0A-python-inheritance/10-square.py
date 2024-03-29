#!/usr/bin/python3
""" This module contains the Square class """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ This is a Square class that inherits from Rectangle class """

    def __init__(self, size):
        """ instantiates the Square class """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Returns the area of the square """
        return self.__size * self.__size
