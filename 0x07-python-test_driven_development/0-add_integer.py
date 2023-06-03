#!/usr/bin/python3
""" This module contains the add_integer function"""


def add_integer(a, b=98):
    """returns the sum.of two inteers"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
