#!/usr/bin/python3
""" This function finds the peak of an unsorted list """


def find_peak(list_of_integers):
    """Find a Peak in a list

    Args:
        list_of_integers: list of int
    Returns:
        the value or None
    """
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return list_of_integers[low]
