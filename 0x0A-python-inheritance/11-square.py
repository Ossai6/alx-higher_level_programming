#!/usr/bin/python3
""" This module contains the Square class """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """ instantiates the Square class """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ returns the area of the asquare """
        return self.__size * self.__size

    def __str__(self):
        """ returns the string representation of a square """
        return (f"[Square] {self.__size}/{self.__size}")
