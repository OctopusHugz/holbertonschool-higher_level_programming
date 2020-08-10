#!/usr/bin/python3
"""This module lists all states from the database hbtn_0e_0_usa matching the
expression the user entered, safe from SQL injection"""
from base import cur, db


def cities_by_state():
    """This function gets all the states matching the expression provided by
the user and prints them row by row, safe from SQL injection"""
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities,
                    states WHERE states.id=cities.state_id
                    """)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == '__main__':
    cities_by_state()
