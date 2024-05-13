#!/usr/bin/python3
"""comment"""
import requests
import sys


if __name__ == "__main__":
    """comment"""
    argv = sys.argv
    q = argv[1] if len(argv) > 1 else ""
    req = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        dic = r.json()
        if dic == {}:
            print('No result')
        else:
            print("[{}] {}".format(dic.get('id'), dic.get('name')))
    except ValueError:
        print('Not a valid JSON')
