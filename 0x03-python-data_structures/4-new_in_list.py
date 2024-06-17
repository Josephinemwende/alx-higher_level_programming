#!/usr/bin/python3
"""A function that replaces an element in a list
at as specific position"""


def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list[:]

    new_list = my_list[:]
    new_list[idx] = element
    return new_list
