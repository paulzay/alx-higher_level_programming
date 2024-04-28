#!/usr/bin/python3

"""comment"""
import sys
import MySQLdb


def main():
  argv = sys.argv
  con = MySQLdb.connect(host="localhost", port=3306,
        user=argv[1], passwd=argv[2],
                         db=argv[3], charset="utf-8")
  cur = con.cursor()
  cur.execute("SELECT * FROM states WHERE name \
    LIKE BINARY 'N%' ORDER BY states.id ASC")
  query_rows = cur.fetchall()
  for row in query_rows:
    print(row)


if __name__ == '__main__':
  main()
