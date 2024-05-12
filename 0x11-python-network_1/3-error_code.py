#!/usr/bin/python3
"""comment"""
import sys
import urllib.request
from urllib.error import HTTPError


def main():
    """comment"""
    argv = sys.argv
    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode("utf-8", "replace"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    main()
