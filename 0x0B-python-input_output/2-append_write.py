#!/usr/bin/python3
"""
This module contains append_write function
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file
    and returns the number of characters added:"""
    with open(filename, 'a', encoding='utf-8') as file:
        chars_written = file.write(text)
        return chars_written
