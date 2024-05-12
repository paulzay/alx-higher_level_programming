#!/usr/bin/python3
"""commment"""
import requests
import sys


def main():
    """comment"""
    argv = sys.argv
    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.text)


if __name__ == "__main__":
    main()
