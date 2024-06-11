#!/usr/bin/python3
# program that imports the function def add(a, b): from the file add_0
if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2
    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))
