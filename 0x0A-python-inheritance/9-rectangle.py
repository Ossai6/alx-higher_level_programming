#!/usr/bin/python3
class BaseGeometry:
    """
    This class contains the "area" method
    """

    def area(self):
        """
        raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the name and value argumentsa
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater that 0".format(name))


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

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns the string representation of the object"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
