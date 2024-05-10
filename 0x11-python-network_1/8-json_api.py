#!/usr/bin/python3
import requests
import sys
"""comment"""


def main:
    """comment"""
    argv = sys.argv
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    req = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        dic = r.json()
        if dic == {}:
            print('No result')
        else:
            print("[{}] {}".format(dic.get('id'), dic.get('name')))
    except ValueError:
        print('Not a valid JSON')
    

if __name__ == "__main__":
    main()
