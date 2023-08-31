#!/usr/bin/python3

def custom_magic_calculation(parameter_a, parameter_b):
    """Perform a custom magic calculation based on the given parameters."""

    magic_result = 0
    for i in range(1, 3):
        try:
            if i > parameter_a:
                raise Exception('Too far')
            else:
                magic_result += parameter_a ** parameter_b / i
        except:
            magic_result = parameter_b + parameter_a
            break
    return (magic_result)
