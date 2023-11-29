#!/usr/bin/python3
def uppercase(str):
    up = []
    for s in str:
        if ord(i) >= 97 and ord(str) <= 122:
            up.append(chr(ord(s) - 32))
        else:
            up.append(s)
    c = ''.join(up)
    print("{}".format(c))
