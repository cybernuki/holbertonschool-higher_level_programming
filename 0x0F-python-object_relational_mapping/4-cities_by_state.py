#!/usr/bin/python3
# This script show all cities
from sys import argv
import MySQLdb


if __name__ == '__main__':
    usr_name, usr_pass, db_name = argv[1], argv[2], argv[3]
    db = MySQLdb.connect(
        host='localhost',
        user=usr_name,
        passwd=usr_pass,
        db=db_name)

    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name FROM cities as c\
    INNER JOIN states as s ON c.state_id = s.id\
    ORDER BY c.id")

    [print(state) for state in cur.fetchall()]
