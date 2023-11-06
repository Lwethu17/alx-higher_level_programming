#!/usr/bin/python3
""" Program that inherits from int class """


class MyInt(int):
    """ Class MyInt that inherits from int """
    def __eq__(self, other):
        """ Equal (=) inverted """
        return False

    def __ne__(self, other):
        "Not equal (!=) inverted """
        return True
