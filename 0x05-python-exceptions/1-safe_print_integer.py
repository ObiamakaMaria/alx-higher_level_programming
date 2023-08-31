#!/usr/bin/python3

def print_formatted_integer(value):
    """Safely print an integer using "{:d}".format()"""

    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
