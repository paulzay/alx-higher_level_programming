#!/usr/bin/python3
import sys


def main():
    argv = sys.argv
    argv.pop(0)
    count = 0
    for num in argv:
        count += int(num)
    print("{}".format(count))


if __name__ == "__main__":
    main()
