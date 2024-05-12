#!/usr/bin/python3
"""comment"""
import requests
import sys


def main():
    """comment"""
    argv = sys.argv
    r = requests.get('https://api.github.com/user',
                     auth=(argv[1], argv[2]))
    if r.status_code >= 400:
        print('None')
    else:
        print(r.json().get('id'))


if __name__ == "__main__":
    main()
