#!/usr/bin/python3
"""
A BaseGeometry class
"""


class BaseGeometry:
    """
    This class contains a method called area
    """
    def area(self):
        """
        This method raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This method validates and sets the name
        and value attributes
        """
        self.name = name
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value > 0:
            self.value = value
        else:
            raise ValueError("{} must be greater than 0".format(name))
