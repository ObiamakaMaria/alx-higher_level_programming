#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
<<<<<<< HEAD
    """Print x elements of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return ret
=======
    """Prints up to x elements from my_list and returns the actual number of printed elements."""
    try:
        count = 0
        for i in my_list:
            if count < x:
                print(i, end=" ")
                count += 1
            else:
                break
        print()
        return count
    except:
        raise
>>>>>>> 8ebc7e532762af5e16b1e0e4d4bbd4408cee8fa3
