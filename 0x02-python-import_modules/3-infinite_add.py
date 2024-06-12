#!/usr/bin/python3
# program that prints the result of the addition of all arguments
if __name__ == "__main__":
    import sys
    for arg in sys.arg[]:
        argv = int(arg)
        print(sum(argv))
