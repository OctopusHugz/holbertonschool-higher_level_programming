#!/usr/bin/python3
"""This module lists all states from the database hbtn_0e_0_usa starting with
N"""
from sys import argv
import MySQLdb


def filter_states():
    """This function gets all the states starting with the letter N
and prints them row by row"""
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id;")
    rows = cur.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)
    cur.close()
    db.close()


if __name__ == '__main__':
    filter_states()
