#!/usr/bin/python3
"""
This module contains load_from_json_file functiom
"""


import json


def load_from_json_file(filename):
    """
    create an object from a JSON file
    """
    with open(filename, 'r', encoding='utf-8') as _file:
        return json.load(_file)
