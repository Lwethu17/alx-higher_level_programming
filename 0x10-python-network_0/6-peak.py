#!/usr/bin/python3
"""The algorithms for a list of integers"""

def find_peak(list_of_integers):
    """Gets the peak in the list of the integers."""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
