#!/usr/bin/python3
"""
This file contains a class MyList that inherets from List
"""


class MyList(list):
    """
    A class that inherits from List
    """
    def __init__(self):
        """ Instantiates the object """
        super().__init__()

    def print_sorted(self):
        """ prints the list, but sorted (ascending sort) """
        print(sorted(self))
