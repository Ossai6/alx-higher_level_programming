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
