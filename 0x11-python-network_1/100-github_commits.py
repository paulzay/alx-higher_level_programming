#!/usr/bin/python3
import requests
import sys
"""comment"""


def main:
    """main"""
    argv= sys.argv
    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(argv[2], argv[1]))
    if r.status_code >= 400:
        print('None')
    else:
        for com in r.json()[:10]:
            print("{}: {}".format(com.get('sha'),com.get('commit').get('author').get('name')))


    if __name__ == "__main__":
        main()
