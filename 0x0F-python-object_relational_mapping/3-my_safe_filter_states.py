#!/usr/bin/python3
"""This module lists all states from the database hbtn_0e_0_usa matching the
expression the user entered, safe from SQL injection"""
from base import cur, db
from sys import argv


def my_safe_filter_states():
    """This function gets all the states matching the expression provided by
the user and prints them row by row, safe from SQL injection"""
    cur.execute("SELECT * FROM states;")
    rows = cur.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    cur.close()
    db.close()


if __name__ == '__main__':
    my_safe_filter_states()
