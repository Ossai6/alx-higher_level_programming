#!/usr/bin/python3
"""
This module contains add_attribute
"""


def add_attribute(obj, att, value):
    """
    This method adds a new attribute to an object if possible.
    Args:
        obj: The object to add an attribute to.
        att: The name of the attribute to add to obj.
        value: The value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, att, value)
    else:
        raise TypeError("can't add new attribute")
