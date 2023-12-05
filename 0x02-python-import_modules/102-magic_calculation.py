#!/usr/bin/python3

def magic_calculation(a, b):

    from magic_calculation_102 import add, sub

    if a < b:

        total = add(a, b)

        for num in range(4, 6):

            total = add(total, num)

        return total

    else:

        return sub(a, b)
