#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for num in range(x):
        try:
            print("{:d}".format(my_list[num]), end='')
            counter += 1
            for n in range(counter):
                print("", end='')
        except (ValueError, TypeError):
            print("", end='')
    print()
    return counter
