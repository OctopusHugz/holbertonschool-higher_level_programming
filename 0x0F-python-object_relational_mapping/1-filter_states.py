#!/usr/bin/python3
"""This module lists all states from the
database hbtn_0e_0_usa starting with N"""
import MySQLdb
from sys import argv


def filter_states():
    """This function gets all the states starting with the letter N
and prints them row by row"""
    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=argv[1], passwd=argv[2], db=argv[3])
        cur = db.cursor()
        cur.execute("""SELECT * FROM states WHERE name LIKE 'N%'
                    ORDER BY states.id ASC;""")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    filter_states()
