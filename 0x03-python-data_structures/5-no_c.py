#!/usr/bin/python3
def no_c(my_string):
    chars = []
    for s in my_string:
        if s != 'c' and s != 'C':
            chars.append(s)
    return ''.join(chars)