#!/usr/bin/python3
import sys


def main():
    count = 0
    argv = sys.argv
    argv.pop(0)
    length = len(argv)

    if length == 0:
        print("{} arguments.".format(length))
    elif length == 1:
        print("{} argument:".format(length))
        print("1: {}".format(argv[0]))
    elif length >= 2:
        print("{} arguments:".format(length))
        for s in argv:
            print("{}: {}".format(count+1, argv[count]))
            count += 1


if __name__ == "__main__":
    main()
