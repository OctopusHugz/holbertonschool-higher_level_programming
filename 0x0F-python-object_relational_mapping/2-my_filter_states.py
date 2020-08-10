#!/usr/bin/python3
"""This module lists all states from the database hbtn_0e_0_usa matching the
expression the user entered"""
from base import cur, db, exec_string


def my_filter_states():
    """This function gets all the states matching the expression provided by
the user and prints them row by row"""
    cur.execute(exec_string)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == '__main__':
    my_filter_states()
