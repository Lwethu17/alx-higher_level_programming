#!/usr/bin/python3
"""


This module is composed by a function that is addition of two numbers.


"""

def add_integer(a, b=98):
    """ A function that is addition of two numbers

    Args:
         a: first integer
         b: second integer

    Returns:
         The results of addition of two numbers

    Raises:
         TypeError: If the numbers given a or b aren't integers

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
