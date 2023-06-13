#!/usr/bin/python3
"""
    This module contains the to_json_string function
"""
import json


def to_json_string(my_obj):
    """ returns the json of an object(string)"""
    string_rep = json.dumps(my_obj)
    return string_rep
