#!/usr/bin/python3
"""comment"""
import sys
import requests


def main():
    """comment"""
    argv = sys.argv
    res = requests.get(argv[1])
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)


if __name__ == "__main__":
    main()
