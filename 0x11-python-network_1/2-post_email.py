#!/usr/bin/python3
import urllib.request
import sys
import urllib.parse
"""coment"""


def main:
    """commment"""
    argv = sys.argv
    var = {'email': argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-'", 'replace'))


if __name__ == "__main__":
    main()
