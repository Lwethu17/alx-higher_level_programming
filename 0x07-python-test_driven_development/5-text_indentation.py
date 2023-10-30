#!/usr/bin/python3
"""

This module is composed by a function that prints 2 new lines after ".?:" characters

"""

def text_indentation(text):
    """ A function that prints 2 new lines after ".?:" characters


    Args: 
       text: string input

    Returns: 
          No return


    Raises:
          TypeError: If the text is not a string.

    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    c = text[:]

    for n in ".?:":
        list_text = c.split(n)
        c = ""
        for m in list_text:
            m = m.strip(" ")
            c = m + n if c is "" else c + "\n\n" + m + n

    print(c[:-3], end="")
