#!/usr/bin/python3
"""
This module contains append_write function
"""


def append_write(filename="", text=""):
    """
    returns the number of characters added
    """
    with open(filename, 'a') as _file:
        return _file.write(text)
