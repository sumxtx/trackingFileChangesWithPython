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
    query = "CREATE TABLE files (file TEXT, md5 TEXT)"
    conn_db = connect_db()
    try:
        if not conn_db is None:
            if not table_exists('files'):
                cursor = conn_db.cursor()
                try:
                    cursor.execute(query)
                except sqlite3.OperationalError:
                    if cursor != None:
                        cursor.close()
                finally:
                    conn_db.commit()
                    if cursor != None:
                        cursor.close()
                    result = True
    except sqlite3.OperationalError as err:
        print(str(err))
        if conn_db != None:
            conn_db.close()
    finally:
        if conn_db != None:
            conn_db.close()
    return result

def create_hash_table_idx():
    # Create a SQLite DB Table Index
    table = 'files'
    query = 'CREATE INDEX idxfile ON files (file, md5)'
    conn_db = connect_db()
    try:
        if not conn is None:
            if table_exists(table):
                cursor = conn_db.cursor
                try:
                    cursor.execute(query)
                except sqlite3.OperationalError:
                    if cursor != None:
                        cursor.close()
                finally:
                    conn_db.commit()
                    if cursor != None:
                        cursor.close()
    except sqlite3.OperationalError as err:
        print(str(err))
        if conn_db != None:
            conn.close()
    finally:
        if conn_db != None:
            conn_db.close()

def run_cmd(qry,args):
    # Run a specific command on the SQLite DB
    conn_db = connect_db()
    try:
        if not conn_db in None:
            if table_exists('files'):
                cursor = conn_db.cursor()
                try:
                    cursor.execute(qry,args)
                except sqlite3.OperationalError:
                    if cursor != None:
                        cursor.close()
    except sqlite3.OperationalError as err:
        print(str(err))
        if conn_db != None:
            conn_db.close()
    finally:
        if conn_db != None:
            conn_db.close()

def update_hash_table(fname, md5):
    # Update the SQLite File Table
    qry = "UPDATE files SET md5=? WHERE file=?"
    args = (md5, fname)
    run_cmd(qry,args)

def insert_hash_table(fname, md5):
    # Insert into the SQLite File Table
    qry = "INSERT INTO files (file, md5) VALUES (?, ?)"
    args = (fname, md5)
    run_cmd(qry)

def setup_hash_table(fname, md5):
    # Set up the hash table
    #Call the create hash table function
    create_hash_table()
    #Call the create index on the has table function
    create_hash_table_idx()

    insert_hash_table(fname, md5)

def md5_in_db(fname):
    # Checks if md5 hash tag exists in the SQLite DB
    items = []
    qry = "SELECT md5 FROM files WHERE file=?"
    args(fname,)
    conn_db = connect_db()
    try:
        if not conn is None:
            if table_exists('files'):
                cursor = conn_db.cursor()
                try:
                    cursor.execute(qry, args)
                    for row in cursor:
                        items.append(row[0])
                except sqlite3.OperationalError as err:
                    print(str(err))
                    if cursor != None:
                        cursor.close()
                finally:
                    if cursor != None:
                        cursor.close()
    except sqlite3.OperationalError as err:
        print(str(err))
        if conn_db != None:
            conn_sb.close()
    finally:
        if conn_db != None:
            conn_db.close()
    return items



