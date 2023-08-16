#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary.keys()):  #This sorts the keys and iterate through them
        print("{}: {}".format(key, a_dictionary[key]))  #Printing key & corresponding value
