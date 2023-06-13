#!/usr/bin/python3
"""
    This module contains the write_file function
"""


def write_file(filename="", text=""):
    """
        Writes a text to a file and returns the
        number of words written
    """
    with open(filename, 'w', encoding="utf-8") as file:
        file = file.write(text)
        return (file)
