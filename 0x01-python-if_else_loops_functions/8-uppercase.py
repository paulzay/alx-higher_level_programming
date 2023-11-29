#!/usr/bin/python3
def uppercase(str):
    up = []
    for s in str:
        if ord(s) >= 97 and ord(s) <= 122:
            up.append(chr(ord(s) - 32))
        else:
            up.append(s)
    c = ''.join(up)
    print("{}".format(c))
