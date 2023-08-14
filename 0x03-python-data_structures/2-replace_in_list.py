#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """This script replaces an element of a list at a particular position."""
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return (my_list)
