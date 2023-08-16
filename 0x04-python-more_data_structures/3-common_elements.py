#!/usr/bin/python3

def common_elements(set_1, set_2):
    common_set = set()  # Empty list to store similar elements
    for element in set_1:
        if element in set_2:
            common_set.add(element)
    return common_set
