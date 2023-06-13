#!/usr/bin/python3
"""
    This module contains from_json_string function
"""

import json


def from_json_string(my_str):
    """ returns the python object from a JSON string"""
    return json.loads(my_str)
