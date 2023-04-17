#!/usr/bin/python3
"""
This module contains the class Base
"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == "":
            return  "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding="utf-8") as _filename:
            if list_objs is None:
                json.dump("[]", _filename)
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                _filename.write(Base.to_json_string(list_dicts))
