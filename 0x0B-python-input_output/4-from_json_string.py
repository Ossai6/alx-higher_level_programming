#!/usr/bin/python3
""" This module contains the to_json_string function """

import json


def to_json_string(my_obj):
    """
    function that returns an object (Python data structure)
    represented by a JSON string:
    """
    return json.loads(my_obj)
