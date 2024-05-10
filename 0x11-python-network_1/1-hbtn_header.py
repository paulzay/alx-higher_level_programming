#!/usr/bin/python3
import urllib.request
import sys
"""urllib header"""


def main:
    """comment"""
    arg = sys.argv
    with urllib.request.urlopen(arg[1]) as response:
        res = response.headers.get('X-Request-Id')
        print(res)


if __name__ == "__main__":
    main()
