#!/usr/bin/python3
"""This module lists all cities by state from the database hbtn_0e_0_usa
matching the expression the user entered, safe from SQL injection"""
import MySQLdb
from sys import argv


def filter_cities():
    """This function gets all the states matching the expression provided by
the user and prints them row by row, safe from SQL injection"""
    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=argv[1], passwd=argv[2], db=argv[3])
        cur = db.cursor()
        cur.execute("""SELECT cities.name FROM cities
                    LEFT JOIN states ON cities.state_id = states.id
                    WHERE states.name = '{}'""".format(argv[4]))
        rows = cur.fetchall()
        for row in rows:
            print(row[0] + ", " if row != rows[-1] else row[0], end='')
        print()
        cur.close()
        db.close()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    filter_cities()
