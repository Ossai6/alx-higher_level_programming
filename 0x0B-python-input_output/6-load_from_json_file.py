#!/usr/bin/python3
"""
h
"""


import json


def load_from_json_file(filename):
    """
    gg
    """
    with open(filename, 'r', encoding='utf-8') as _file:
        return json.load(_file)
