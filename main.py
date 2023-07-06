"""
- [] Create and connect to a local SQLite database
        Usage of the built-in Python OS, sys, and SQLite libraries
        Write a series of Python functions that can create an SQLite instance
        Write a Python function that can query the master database for the SQLite instance created
        Write a series of Python functions that can create and connect to a database hosted within the SQLite instance
"""

import sqlite3
import os
import sys

def get_db_filename():
    """ Name of the SQLite DB file"""
    return os.path.splitext(os.path.basename(__file__))[0]

conn_db = sqlite3.connect("datafile.db")
cursor = conn_db.cursor()


# Some inserting examples
cursor.execute("create table people (id integer primary key, name text, count integer)")

cursor.execute("insert into people (name,count) values ('Bob', 1)")

cursor.execute("insert into people (name, count) values (?,?)", ("Jill", 15))

cursor.execute("insert into people (name, count) values (:username, :usercount)", {"username": "Joe", "usercount":10})

conn_db.commit()

result = cursor.execute("select * from people")
print(result.fetchall())

conn_db.close()
