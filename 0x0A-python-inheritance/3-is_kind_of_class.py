#!/usr/bin/python3
"""
    3-is_kind_of_class: is_kind_of_class()
"""

def is_kind_of_class(obj, a_class):
    """
        returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class.
        Args:
             obj (object): object.
             a_class (class): class.
        Return: True or false.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
