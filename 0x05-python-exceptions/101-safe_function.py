#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Safely executes a given function[[O.

    Args:
        fct: The function to be  executed.
        args: Arguments to the function.

    Returns:
        Upon reaching an error - None.
        Otherwise - result of the call to function.
    """
    try:
        fct_result = fct(*args)
        return (fct_result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
