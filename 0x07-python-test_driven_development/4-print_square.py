#!/usr/bin/python3
"""
This is the module for printing square with #
"""


def print_square(size):
    """Function for printing of square with #

    Args:
         size: (int always) >= 0
    Raises
        TypeError: If the size is not int
        ValueError: If the size is less than error
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("") 
