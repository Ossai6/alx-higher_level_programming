#!/usr/bin/python3
"""
A function that returns the list of available
attributes and methods of an object
"""


def lookup(obj):
    """
    listing all the attributes and methos
    of the object
    """
    lst = dir(obj)
    return lst
