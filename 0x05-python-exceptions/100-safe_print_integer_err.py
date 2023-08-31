#!/usr/bin/python3

import sys

def print_safe_integer(value):
    """Prints an integer using the "{:d}".format() method.

    If a ValueError is caught, an appropriate error message is printed to the standard error stream.

    Args:
        value (int): The integer value to be printed.

    Returns:
        bool: True if the integer was printed successfully, False if a TypeError or ValueError occurred.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Error: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
