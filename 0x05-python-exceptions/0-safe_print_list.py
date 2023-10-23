#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.

    Args:
       my_list (list): The list to print elements from list.
       x (int): The number of elements of my_list to be printed.



    Returns:
       The real number of elements to be printed.
    """
    elements_printed = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            elements_printed += 1
        except IndexError:
            break
    print("")
    return (elements_printed)
