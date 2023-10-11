#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    list_ord = list(a_dictionary.keys())
    list_ord.sort()
    for c in list_ord:
        print("{}: {}".format(c, a_dictionary.get(c)))
