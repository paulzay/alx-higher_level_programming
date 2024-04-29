#!/usr/bin/python3

""" comment """
import sys
import MySQLdb


def main():
    argv = sys.argv
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name, states.name FROM cities \
            INNER JOIN states ON cities.state_id = states.id \
            ORDER BY cities.id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    main()
