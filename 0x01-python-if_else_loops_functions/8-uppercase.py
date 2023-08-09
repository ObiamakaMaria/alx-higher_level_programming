#!/usr/bin/python3

def uppercase(str):
    """Print a string in uppercase."""
    new_word = True
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            c = chr(ord(c) - ord('a') + ord('A'))
        if new_word:
            print("{}".format(c), end="")
            new_word = False
        else:
            print(" {}".format(c), end="")
        if c == ' ':
            new_word = True
