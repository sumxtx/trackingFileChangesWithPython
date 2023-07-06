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

def get_basefile():
    #Name of the script
    return os.path.splitext(os.path.basename(__file__))[0]

def connect_db():
    #Connect to the SQLite DB
    try:
        db_filename = get_basefile() + '.db'
        db_conn = sqlite3.connect(db_filename, timeout=2)
    except BaseException as err:
        print(str(err))
        db_conn = None
    return db_conn

def core_cursor(db_conn, query, args):
    #Opens a SQLite DB Cursor
    result = False
    cursor = db_conn.cursor()
    try:
        cursor.execute(query, args)
        rows = cursor.fetchall()
        num_rows = len(list(rows))
        if num_rows > 0:
            result = True
    except sqlite3.OperationalError as err:
        print(str(err))
        if cursor != None:
            cursor.close()
    finally:
        if cursor != None:
            cursor.close()
    return result

def table_exists(table):
    #Checks if a SQLite DB Table already exists
    result = False
    conn_db = connect_db()
    try:
        if not conn_db is None:
            db_querry = "SELECT name from sqlite_master WHERE type='table' AND name=?"
            args = (table,)
            result = core_cursor(conn_db, db_querry, args)
            if conn_db != None:
                conn_db.close()
    except sqlite3.OperationalError as err:
        print(str(err))
        if conn_db != None:
            conn_db.close()
    return result

def create_hash_table():
    # Create a SQLite DB Table
    result = False
    query = "CREATE TABLE hashs (id integer primary key, filename text, hash )"
    try:
        conn_db = connect_db()
        if not conn_db is None:
            if not table_exists('files'):
                try:
                    cursor = conn.cursor()
                    cursor.execute(query)
                    #
    return result

def create_hash_table_idx():
    # Create a SQLite DB Table Index
    table = 'files'
    query = 'CREATE INDEX idxfile ON ...'
    try:
        conn_db = connect_db()
        if not conn is None:
            if not table_exists(table):
                try:
                    cursor = conn.cursor
                    cursor.execute(query)
                    #

def run_cmd(qry):
    # Run a specific command on the SQLite DB
    try:
        conn = connect_db()
        if not conn in None:
            if table_exists('files'):
                try:
                    cursor = conn.cursor()
                    cursor.execute(qry)
                    #

def update_hash_table(fname, md5):
    # Update the SQLite File Table
    qry = "UPDATE files ..."
    runcmd(qry)

def insert_hash_table(fname, md5):
    # Insert into the SQLite File Table
    qry = "INSERT INTO files..."
    run_cmd(qry)

def setup_hash_table(fname, md5):
    #Call the create hash table function
    #Call the create index on the has table function
    insert_hash_table(fname, md5)

def md5_in_db(fname):
    items = []
    qry = "SELECT ..."
    try:
        conn = connect_db()
        if not conn is None:
            if table_exists('files'):
                try:
                    cursor = conn.cursor()
                    cursor.execute(qry)
                    #
    return items



