#!/usr/bin/python3

def print_list_integer(my_list=[]):
    my_list = [1, 2, 3, 4, 5]
    for values in my_list:
        print(str.format("{}", values))


print_list_integer()
