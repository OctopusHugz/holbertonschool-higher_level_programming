#!/usr/bin/python3
"""This module lists all states from the database hbtn_0e_0_usa"""
from sys import argv
import MySQLdb


def select_states():
    """This function gets all the states and prints them row by row"""
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == '__main__':
    select_states()
