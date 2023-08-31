#!/usr/bin/python3

def magic_calculation(a, b):
    magic_result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                magic_result += a ** b / i
        except Exception as e:
            magic_result = b + a
            break
    return (magic_result)
