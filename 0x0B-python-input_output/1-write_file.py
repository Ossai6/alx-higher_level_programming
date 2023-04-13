#!/usr/bin/python3
"""
This module contains the write_function
"""


def write_file(filename="", text=""):
    """
    This function writes a text to.a file
    """
    with open(filename, 'w', encoding="utf-8") as _file:
        return _file.write(text)
