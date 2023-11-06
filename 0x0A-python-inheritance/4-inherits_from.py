#!/usr/bin/python3
"""
   4-inherits_from: inherits_from()
"""


def inherits_from(obj, a_class):
    """
    returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
    """

    if not isinstance(a_class, type):
        raise TypeError("a_class type must be type")
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
