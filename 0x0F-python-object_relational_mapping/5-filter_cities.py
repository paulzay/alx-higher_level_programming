#!/usr/bin/python3

"""COMMENT"""
import sys
import MySQLdb


def main():
    argv = sys.argv
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities WHERE name=%s\
            LEFT JOIN states ON cities.states.id = states.id".format(argv[4]))
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))


if __name__ == '__main__':
    main()
