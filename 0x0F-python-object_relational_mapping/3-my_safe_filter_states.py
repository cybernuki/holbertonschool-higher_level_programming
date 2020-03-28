#!/usr/bin/python3
# This script avoids sql injections
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
    cur.execute("SELECT * FROM states")

    [print(state) for state in cur.fetchall() if state[1] == search]
