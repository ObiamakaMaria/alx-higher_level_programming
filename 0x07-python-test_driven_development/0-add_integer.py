#!/usr/bin/python3

"""
Module to add two integers or floats.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    :param a: The first integer or float.
    :param b: The second integer or float (default is 98).
    :return: The addition of a and b as an integer.
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    return (int (a) + int (b))
