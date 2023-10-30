#!/usr/bin/python3
"""

This module is composed by a function that multiplys 2 matrices

"""


def matrix_mul(m_a, m_b):
    """ A funtion that multiplies 2 matrices.


    Args:
        m_a: matrix a 
        m_b: matrix b

    Returns: 
           The result gotten after multiplication

    Raises:
          TypeError: if m_a or m_b aren't a list
          TypeError: if m_a or m_b aren't a list of a lists
          ValueError: if m_a or m_b are empty
          TypeError: if the lists of m_a or m_b don't have integers
          TypeError: if the rows of m_a or m_b don't have the same size
          ValueError: if m_a and m_b can't be multiplied


    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for elems in m_a:
        if not isinstance(elems, list):
            raise TypeError("m_a must be a list of lists")

    for elems in m_b:
        if not isinstance(elems, list):
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for lists in m_a:
        for elems in lists:
            if not type(elems) in (int, float):
                raise TypeError("m_a should contain only integers or floats")

    for lists in m_b:
        for elems in lists:
            if not type(elems) in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    width = 0

    for elems in m_a:
        if width != 0 and width != len(elems):
            raise TypeError("each row of m_a must be of the same size")
        width = len(elems)

    width = 0

    for elems in m_b:
        if width != 0 and width != len(elems):
            raise TypeError("each row of m_b must be of the same size")
        width = len(elems)

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    c1 = []
    d1 = 0

    for a in m_a:
        c2 = []
        d2 = 0
        temp = 0
        while (d2 < len(m_b[0])):
            temp += a[d1] * m_b[d1][d2]
            if d1 == len(m_b) - 1:
                d1 = 0
                d2 += 1
                c2.append(temp)
                temp = 0
            else:
                d1 += 1
        c1.append(c2)

    return c1
