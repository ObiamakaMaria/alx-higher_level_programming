#!/usr/bin/python3

def safe_divide(a, b):
    """Divide two numbers 'a' by 'b' safely and return the result.

    This function attempts to divide 'a' by 'b'.
    """
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print("Result of division: {}".format(result))
    return result
