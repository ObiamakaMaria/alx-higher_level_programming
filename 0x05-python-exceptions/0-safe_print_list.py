#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    """Safely prints up to x elements from a list """

    printed_count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            printed_count += 1
        except IndexError:
            break
    print("")
    return (printed_count)
