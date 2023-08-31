#!/usr/bin/python3

def print_first_x_integers(input_list=[], num_elements=0):
    """Safely print the first 'num_elements' integers from a given list.

    Args:
        input_list (list): The list containing elements to print from.
        num_elements (int): The number of integer elements to print.

    Returns:
        int: The count of successfully printed integer elements.
    """
    printed_count = 0
    for i in range(0, num_elements):
        try:
            print("{:d}".format(input_list[i]), end="")
            printed_count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return printed_count
