#!/usr/bin/python3

def print_last_digit(number):
    """This function actually print the last digit of a number and return it."""
    print(abs(number) % 10, end="")
    return (abs(number) % 10)
