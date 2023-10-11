#!/usr/bin/python3
#2-uniq_add.py

def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    num = 0

    for c in uniq_list:
        num += c

    return (num)
