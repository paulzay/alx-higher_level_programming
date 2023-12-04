#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for num in reversed(my_list):
        print("{:d}".format(num))
print_reversed_list_integer(my_list=[1,2,3,4,5])
