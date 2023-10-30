#!/usr/bin/python3
"""

This module is composed by a function that prints a square with character #

"""

def print_square(size):
    """ A functin that prints a square with the character #

    Args:
       size: The square size printed

    Returns:
         No return

    Raises:
        TypeError: If size is not an integer number


    """
    
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size > 0:
        raise ValueError("size must be >= 0")

    for n in range(size):
        print("#" * size)
