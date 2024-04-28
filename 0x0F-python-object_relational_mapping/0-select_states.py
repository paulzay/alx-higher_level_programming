#!/usr/bin/python3

""" comment """

import MySQLdb
import sys


def main():
    print('hello')
    argv = sys.argv
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2],
                         db=argv[3], charset="utf-8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)


if __name__ == "__main__":
    main()
