#!/usr/bin/python3
"""comment"""
import requests
import sys


def main():
    """comment"""
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))


if __name__ == "__main__":
    main()
