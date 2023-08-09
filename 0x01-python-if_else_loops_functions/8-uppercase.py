#!/usr/bin/python3

def uppercase(str):
    """Print a string in uppercase."""
    first_line = True
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            c = chr(ord(c) - ord('a') + ord('A'))
        if first_line:
            print("\n{}".format(c), end="")
            first_line = False
        else:
            print("{}".format(c), end="")
