#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element 2 lists.

    Args:
    my_list_1 (list): The first list of elements.
    my_list_2 (list): The second list of elements.
    list_length (int): The number of elements to divide.

    Returns:
    A new list (length = list_length) with all divisions.
    """
    result_list = []
    for n in range(0, list_length):
        try:
            div = my_list_1[n] / my_list_2[n]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            result_list.append(div)
    return (result_list)
