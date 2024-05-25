#!/usr/bin/python3
"""
print numbers from 0 to 99
Separated by a comma
Ascending order, with two digits
"""
for numbers in range(0, 100):
    print("{:02d},".format(numbers), end="")
print()
