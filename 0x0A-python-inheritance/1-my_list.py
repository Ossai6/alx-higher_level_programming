#!/usr/bin/python3
"""This module contains the class MyList"""


class MyList(list):
    """
        This is a class "MyList" that inherits from list
    """

    def print_sorted(self):
        """
            prints the list in a sorted order
        """
        print(sorted(self))
