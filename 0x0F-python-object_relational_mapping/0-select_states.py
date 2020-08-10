#!/usr/bin/python3
"""This module lists all states from the database hbtn_0e_0_usa"""
from base import cur, db
import MySQLdb

def select_states():
    """This function gets all the states and prints them row by row"""
    cur.execute("SELECT * FROM states;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == '__main__':
    select_states()
