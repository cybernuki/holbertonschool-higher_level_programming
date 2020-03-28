#!/usr/bin/python3
# This script filter a value in the table
from sys import argv
import MySQLdb


if __name__ == '__main__':
    usr_name, usr_pass, db_name, search = argv[1], argv[2], argv[3], argv[4]
    db = MySQLdb.connect(
        host='localhost',
        user=usr_name,
        passwd=usr_pass,
        db=db_name)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name in ('{}')".format(
        search))

    [print(state) for state in cur.fetchall()]
