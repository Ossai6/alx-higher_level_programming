#!/usr/bin/python3
"""
A class 'Rectangle' that defines a retangle
"""


class Rectangle:
    """
    Defining the class Rectabgle
    """
    def __init__(self, width=0, height=0):
        """
        Instantiating an object with width
        and height attributes
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        A 'get' method that gets the width of a
        private instance attribute
        Return: returns the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        This method sets or modifies the width attribute
        Return: None
        """
        if type(value) is int:
            if (value) < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """
        A 'get' method that gets the heught of a
        private instance attribute
        Return: returns the width
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        This method sets or modifies the height attribute
        Return: None
        """
        if type(value) is int:
            if (value) < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """
        This method computes the area of a rectamgle
        Return: returns the area
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """
        This method computes the perimeter of a rectamgle
        Return: returns the perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width)*2) + ((self.__height)*2)

    def __str__(self):
        new_string = ""
        if self.__width == 0 or self.__height == 0:
            return new_string
        else:
            new_string += "\n".join("#" * self.__width
                                    for j in range(self.__height))
        return new_string
