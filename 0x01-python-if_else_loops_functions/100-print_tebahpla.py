#!/usr/bin/python3
for s in reversed(range(97, 123)):
    if s % 2 != 0:
        print("{:c}".format(s - 32), end='')
    else:
        print("{:c}".format(s), end='')
