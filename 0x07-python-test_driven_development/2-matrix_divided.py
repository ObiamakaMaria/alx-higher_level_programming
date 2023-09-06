#!/usr/bin/python3
"""
This function divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divide through by mtrix

    Args:
        matrix: This is the list of list of int or float
        div: This is the divisor

    Raises:
        Typerror: if matrix is not the list of list
        Typeerror: if  the matrix is not regular
        Typeerror: if the matrix contain anthing other than int & float
        Typeerror: if divisor is not a number or divisor is 0

    Returns:
        The new list without mutatng original list
    """
    if (not isinstance(matrix, list)
        or matrix == []
        or not all(isinstance(num, list) for num in matrix)
        or not all((isinstance(elem, int))
                   or (isinstance(elem, float))
                   for elem in [a for b in matrix for a in b])):
        raise TypeError("matrix must be a matrix (list of lists)\
        of integers/floats")
    if not (all(len(a) == len(matrix[0]) for a in matrix)):
        raise TypeError("Each row of the matrix must have the same size")
    if not ((isinstance(div, int)) or (isinstance(div, float))):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError('division by zero')
    return ([list(map((lambda x: round(x / div, 2)), row)) for row in matrix])
