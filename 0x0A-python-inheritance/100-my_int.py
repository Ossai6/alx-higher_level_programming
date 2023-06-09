#!/usr/bin/python3
"""
    This module contains a class "int", and a subclass "MyInt"
"""


class MyInt(int):
    """
        represents MyInt class, and modifies two methods
    """
    def __eq__(self, number):
        """returns False if the number is an int"""
        if super().__eq__(number):
            return False
        else:
            return True

    def __ne__(self, number):
        """ returns true if the number is not an int"""
        if super().__eq__(number):
            return True
        else:
            return False
