#!/usr/bin/python3
"""
    This module contains the is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """
        returns True if the object is an instance of,
        or if the object is an instance of a class that
        inherited from, the specified class ; otherwise False
    """
    if isinstance(obj, a_class) or type(obj) == a_class:
        return True
    else:
        return False
