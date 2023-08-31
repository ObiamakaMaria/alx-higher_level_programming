#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Safely prints up to x elements from a list and returns the count of printed elements.
    
    Args:
        my_list (list): The list containing elements to be printed.
        x (int): The maximum number of elements to print.
    
    Returns:
        int: The actual number of elements printed.
    """
    printed_count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            printed_count += 1
        except IndexError:
            break
    print("")
    return (printed_count)
