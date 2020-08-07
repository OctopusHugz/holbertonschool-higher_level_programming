#!/usr/bin/python3
"""This module lists all states from the database hbtn_0e_0_usa matching the
expression the user entered"""
import MySQLdb
from sys import argv


def my_filter_states():
    """This function gets all the states matching the expression provided by
the user and prints them row by row"""
    try:
        string = "SELECT * FROM states WHERE name = '" + argv[4] + "'"
        db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
        cur = db.cursor()
        cur.execute(string)
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
    except:
        pass


if __name__ == '__main__':
    my_filter_states()
