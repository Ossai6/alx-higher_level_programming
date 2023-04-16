#!/usr/bin/python3
"""
This module contains the class Base
"""


class Base(object):
    """
    This represents the base class
    Represents the "base" for all other classes in this project.
    Attributes:
        __nb_objects (int): The number of instantiation of the Base.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
         initializes the base
         Args
            id(int): The identity of any base created
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
