#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    num_1 = 0
    den_1 = 0

    for tup in my_list:
        num_1 += tup[0] * tup[1]
        den_1 += tup[1]

    return (num_1 / den_1)
