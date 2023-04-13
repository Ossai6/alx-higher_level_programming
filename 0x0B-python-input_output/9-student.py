#!/usr/bin/python3
"""
This module contains the Student class
"""


class Student:
    """
    A Student class that contains three attributes
    and a method to_json
    """
    def __init__(self, first_name, last_name, age):
        """
        instantiating the object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        This method returns a dictionary representation
        of the Student class
        """
        return self.__dict__
