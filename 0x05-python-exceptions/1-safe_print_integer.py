#!/usr/bin/python3

def safe_print_integer(value):
    """Print an integer with "{:d}".format().

    Args:
    value (int): The integer to be printed.

    Returns:
    If value has been correctly printed (means the value is an integer) - True
    Otherwise - False
    """
    try:
        print("{:d}".format(value))
        return (True)
    except TypeError:
        return (False)
    except ValueError:
        return (False)
