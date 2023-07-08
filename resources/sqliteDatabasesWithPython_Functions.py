import sqlite3


def show_all():
    # Show all records in a db
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit()
    conn.close()

def add_one(arg1,arg2,arg3):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    # Add a record to one table
    c.execute("INSERT INTO tablename VALUES(?,?,?)",(arg1,arg2,arg3))
    
    conn.commit()
    conn.close()

def del_one(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("")


    

