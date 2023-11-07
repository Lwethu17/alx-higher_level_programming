#!/usr/bin/python3
""" module that returns the dictionary description with a simple
data structure for a json serialization of an object
"""


def class_to_json(obj):
    """ function that returns the dictionary description of an object """

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
