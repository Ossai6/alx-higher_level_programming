#!/usr/bin/python3
"""
Defines a class Square
"""


class Square:
    """ A class named Square
    Attributes:
        __size(int): The size of a side of the square
    """
    def __init__(self, size=0):
        """This method initializes a square
        Args:
            size(int = 0): The size of a side of the square
        Returns: None.
        """
        self.__size = size

    def area(self):
        """This method computea the area of a square
        Args:
            self: The object
        Returns: The area of a square
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """This method returns the size of a square
        Args:
            self: The object
        Returns: The size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """This method validates the value of size of a square
        Args:
            value(int): The size of a side of the square
        Returns: None.
        """
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        if self.__size == 0:
            print()
        for x in range(self.__size):
            print("".join(["#" for y in range(self.__size)]))
