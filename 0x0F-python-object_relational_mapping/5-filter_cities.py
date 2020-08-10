#!/usr/bin/python3
"""This module lists all cities by state from the database hbtn_0e_0_usa
matching the expression the user entered, safe from SQL injection"""
from base import cur, db
from sys import argv


def filter_cities():
    """This function gets all the states matching the expression provided by
the user and prints them row by row, safe from SQL injection"""
    cur.execute("""SELECT cities.name FROM cities
                    LEFT JOIN states ON cities.state_id = states.id
                    WHERE states.name = '{}'""".format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row[0] + ", " if row != rows[-1] else row[0], end='')
    print()
    cur.close()
    db.close()


if __name__ == '__main__':
    filter_cities()
