#!/usr/bin/python3
"""
    4-from_json_string: from_json_string()
"""


import json


def from_json_string(my_str):
    """
        Returns an object(python data structure) represented by a json string.
    """
    return (json.loads(my_str))
