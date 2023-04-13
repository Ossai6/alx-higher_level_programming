#!/usr/bin/python3
"""
This module contains save_to_json_file function
"""


import json


def save_to_json_file(my_obj, filename):
    """
    writes an object to a file
    """
    with open(filename, 'w', encoding="utf-8") as _file:
        json.dump(my_obj, _file)
