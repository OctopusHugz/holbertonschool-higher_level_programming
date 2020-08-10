#!/usr/bin/python3
"""This module creates some db and cursor objects"""
from sys import argv
import MySQLdb


db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
cur = db.cursor()
exec_string = """SELECT * FROM states WHERE name
    LIKE BINARY '{}';""".format(argv[4])
