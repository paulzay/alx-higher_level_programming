#!/usr/bin/python3

""" comment """

import sys
import MySQLdb


def main:
    argv = sys.argv
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2],
                         db=argv[3], charset="utf-8")
    cur = db.cursor()


if __name__ == '__main__':
	main()
