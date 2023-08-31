#!/usr/bin/python3

def safe_print_division(a, b):
    """Divide two numbers 'a' by 'b' safely & return the result"""

    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print("Result of division: {}".format(result))
    return (result)
