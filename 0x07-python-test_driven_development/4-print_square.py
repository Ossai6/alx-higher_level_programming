#!/usr/bin/python3
"""
g
"""
def print_square(size):
    """
    g
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#"*size + "\n") * size, end="")
