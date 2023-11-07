#!/usr/bin/python3
""" module that contains a function that returns the json
representation of an object(string).
"""
import json


def to_json_string(my_obj):
    """ function that returns the json representation of an object(string).

    Args:
        my_obj: object

    raises:
        exception: when the object can't be encoded.

    """
    return json.dumps(my_obj)
