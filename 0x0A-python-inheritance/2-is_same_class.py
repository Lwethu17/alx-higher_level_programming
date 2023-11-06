#!/usr/bin/python3
"""
   2-is_same_class: is_same_class()
"""

def is_same_class(obj, a_class):
    """
    returns true if object is exactly an instance of the specified class.
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class must be a type")
    return (type(obj) is a_class)
