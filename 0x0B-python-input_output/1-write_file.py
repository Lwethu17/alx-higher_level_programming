#!/usr/bin/python3
""" module that contains a function that writes to a text file
"""


def write_file(filename="", text=""):
    """ Function that writes a string to text file.

    Args:
        Filename: filename
        Text: text to be written

    raises
        exception: when the file can be opened

    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
