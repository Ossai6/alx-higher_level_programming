#!/usr/bin/python3
"""
This module contains the from_json_string function
"""


import json


def from_json_string(my_str):
    """
    returning an object  data structure) represented
    by a JSON string
    """
    return json.loads(my_str)
