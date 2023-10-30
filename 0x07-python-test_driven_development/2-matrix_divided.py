#!/usr/bin/python3
"""

This module is composed by a function that divides a matrix of numbers.

"""

def matrix_divided(matrix, div):
    """ A function that divides a number of matrix

    Args:
        matrix: list of integers
        div: an integer that divides the matrix

    Returns:
           A whole new matrix with results of division

    Raises:
          TypeError: If the elements of the matrix aren't lists
                     If the elements of the list aren't integers
                     If div is not an integer
                     If the lists of the matrix don't have the same size

          ZeroDivisionError: If div is zero

    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg_type = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_type)

    len_e = 0
    msg_size = "Each row of the matrix must have the same size"

    for elems in matrix:
        if not elems or not isinstance(elems, list):
            raise TypeError(msg_type)

        if len_e != 0 and len(elems) != len_e:
            raise TypeError(msg_size)

        for temp in elems:
            if not type(temp) in (int, float):
                raise TypeError(msg_type)

        len_e = len(elems)

    n = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (n)
