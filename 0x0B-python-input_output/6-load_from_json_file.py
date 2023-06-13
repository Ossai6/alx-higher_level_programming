#!/usr/bin/python3
"""
    This module contains a function
"""

import json


def load_from_json_file(filename):
    """ creates and returns an object from JSON file """
    with open(filename, 'r', encoding="utf-8") as file:
        json_data = file.read()
        return json.loads(json_data)
