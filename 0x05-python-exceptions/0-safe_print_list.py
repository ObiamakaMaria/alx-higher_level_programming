#!/usr/bin/python3

ef safe_print_list(my_list=[], x=0):
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
