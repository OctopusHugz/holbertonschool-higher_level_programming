#!/usr/bin/python3
"""This module lists all states from the database hbtn_0e_0_usa matching the
expression the user entered"""
import MySQLdb
from sys import argv


def my_filter_states():
    """This function gets all the states matching the expression provided by
the user and prints them row by row"""
    string = """SELECT * FROM states WHERE name
    LIKE BINARY '{}';""".format(argv[4])
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute(string)
    rows = cur.fetchall()
    for row in rows:
        # if row[1] == argv[4]:
        print(row)
    cur.close()
    db.close()


if __name__ == '__main__':
    my_filter_states()
