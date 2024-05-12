#!/usr/bin/python3
"""comment"""
import requests


def main():
    """comment"""
    r = requests.get('https://intranet.hbtn.io/status')
    print('Body response:'):
    print('\t- type: {}'.format(type(r.text)))
    print('\t- content: {}'.format(r.text))


if __name__ == "__main__":
    main()
