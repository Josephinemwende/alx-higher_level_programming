#!/usr/bin/python3
"""A function that replaces an element in a list
at as specific position"""
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list[:]
    if idx > len(my_list):
        return my_list[:]
    my_list[element] = idx
    return my_list
