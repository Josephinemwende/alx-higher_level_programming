#!/usr/bin/python3
# program that imports the function def add(a, b): from the file add_0
from add_0 import add
if __name__ == "__main__":
    a = 1
    b = 2
    sum = add(a, b)
    print(f"{a} + {b} = {sum}")