#!/usr/bin/python3
import requests
import sys
"""comment"""


def main:
    """comment"""
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))


if __name__ == "__main__":
    main()
