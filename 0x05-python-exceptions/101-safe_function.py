#!/usr/bin/python3

import sys

def execute_safely(function, *args):
    """Safely executes a given function with provided arguments.

    Args:
        function: The function to be executed.
        args: Arguments to be passed to the function.

    Returns:
        Any: The result of the function call if successful, otherwise None.
    """
    try:
        execution_result = function(*args)
        return (execution_result)
    except Exception:
        print("Error: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
