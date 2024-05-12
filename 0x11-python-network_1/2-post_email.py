#!/usr/bin/python3
"""coment"""
import urllib.request
import sys
import urllib.parse


def main():
    """commment"""
    argv = sys.argv
    var = {'email': argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8', 'replace'))


if __name__ == "__main__":
    main()
