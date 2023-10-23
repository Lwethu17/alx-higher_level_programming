#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list that are integers.


    Args:
    my_list (list): The list to print elements from the list.
    x (int): The number of elements of my_list to be printed.

    Returns:
    The real number of integers printed
    """
    elements_printed = 0
    for n in range(0, x):
        try:
            print("{:d}".format(my_list[n]), end="")
            elements_printed += 1
            except (ValueError, TypeError):
                continue
            print("")
            return (elements_printed)
