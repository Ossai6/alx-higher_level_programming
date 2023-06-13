#!/usr/bin/python3
"""
    This module contains the cStudent class
 """


class Student:
    """Represents the student class"""
    def __init__(self, first_name, last_name, age):
        """ instantiating a Student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns the dictionary representation of a instance object"""
        if attrs is None or not attrs:
            return {"first_name": self.first_name, "last_name":
                    self.last_name, "age": self.age}
        else:
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}
