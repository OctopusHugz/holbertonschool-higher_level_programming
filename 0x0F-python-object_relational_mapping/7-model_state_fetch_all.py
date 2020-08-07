#!/usr/bin/python3
"""This module lists all State objects from the database hbtn_0e_6_usa"""
import MySQLdb
from sys import argv
from model_state import Base, State


def model_state_fetch_all():
    """This function lists all State objects from the database hbtn_0e_6_usa"""
    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=argv[1], passwd=argv[2], db=argv[3])
        cur = db.cursor()
        cur.execute("SELECT * FROM states;")
        rows = cur.fetchall()
        for row in rows:
            print(str(row[0])+ ": " + str(row[1]))
        cur.close()
        db.close()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    model_state_fetch_all()
