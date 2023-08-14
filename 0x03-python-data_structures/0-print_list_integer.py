#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """This script prints all integers of the (my_list)list."""
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
