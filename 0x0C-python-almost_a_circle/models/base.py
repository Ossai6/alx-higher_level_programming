#!/usr/bin/python3
"""
This module contains the Base class
"""
import json


class Base:
    """this class represents the base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """conditionally setting the value of id"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        that writes the JSON string representation of list_objs
        to a file
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        json_string = cls.to_json_string([obj.to_dictionary()
                                          for obj in list_objs])
        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    def update(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes.
        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        # Create a dummy instance
        dummy_instance = cls(1, 1)

        dummy_instance.update(**dictionary)

        # Return the dummy instance with the attributes set
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
         returns a list of instances
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r') as file:
                json_data = file.read()
                instances_data = cls.from_json_string(json_data)
                instances = [cls.create(**data) for data in instances_data]
                return instances
        except FileNotFoundError:
            return []
