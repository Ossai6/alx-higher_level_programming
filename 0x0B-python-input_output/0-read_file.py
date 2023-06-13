#!/usr/bin/python3
"""
    This module contains the read_file function
"""


def read_file(filename=""):
    """
        This function reads and prints a text file(UTF8)
    """
    with open(filename, 'r', encoding="utf-8") as file:
        file = file.read()
        print(file, end="")
