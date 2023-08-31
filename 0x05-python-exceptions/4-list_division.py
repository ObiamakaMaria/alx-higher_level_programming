#!/usr/bin/python3

def divide_lists_elementwise(list1, list2, length):

    """Divides elements of two lists element-wise. """

    division_result_list = []
    for i in range(0, length):
        try:
            div_result = list1[i] / list2[i]
        except TypeError:
            print("Error: Incorrect data type")
            div_result = 0
        except ZeroDivisionError:
            print("Error: Division by zero")
            div_result = 0
        except IndexError:
            print("Error: Index out of range")
            div_result = 0
        finally:
            division_result_list.append(div_result)
    return (division_result_list)
