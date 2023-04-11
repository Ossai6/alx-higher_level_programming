#!/usr/bin/python3
"""
This is  a class MyList that inherits from
the in-built list class.
"""


class MyList(list):
    """
    A subclass of the list class
    """
    def __init__(self):
        """
        initializes the list by calling the
        parent's init magic method
        """
        super().__init__()

    def print_sorted(self):
        """
        prints the list in a sorted ascending
        order
        """
        sorted_list = sorted(self)
        print(sorted_list)
