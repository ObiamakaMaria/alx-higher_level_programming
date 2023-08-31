#!/usr/bin/python3

def print_formatted_integer(value):
    """Safely print an integer using "{:d}".format().

    Args:
        value (int): The integer value to be printed.

    Returns:
        bool: True if the integer was printed successfully, False if a TypeError or ValueError occurred.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
