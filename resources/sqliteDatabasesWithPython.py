import sqlite3

conn = sqlite3.connect("./datafile.db")

#### Create a cursor
cursor = conn.cursor()
#conn.commit() make changes permanent in the database as conn.close() doesn't autommatically commit any changes



#### Create a table

#cursor.execute("create table people (id integer primary key, name text, count integer)") # One liner
    # Data types
        # NULL
        # INTEGER 
        # REAL 
        # TEXT 
        # BLOB 
cursor.execute(""" CREATE TABLE tablename (
    first_name DATATYPE,
    last_name DATATYPE,
    email DATATYPE
    )""") # Multiple Lines

#conn.commit()



#### Insert data into a table

cursor.execute("INSERT INTO tablename VALUES ('John','Elder', 'john@codemy.com')") # One Insertion
#cursor.execute("insert into people (name,count) values ('Bob', 1)")
#cursor.execute("insert into people (name, count) values (?,?)", ("Jill", 15))
#cursor.execute("insert into people (name, count) values (:username, :usercount)", {"username": "Joe", "usercount":10})

many_customers = [('Wes', 'Brown', 'wes@brown.com'),
                  ('Steph','Kuwe', 'steph@kuwea.com'),
                  ('Dan', 'Pas', 'dan@pas.com'),
                  ]
cursor.executemany("INSERT INTO tablename VALUES (?,?,?)", many_customers) # May insertions

#conn.commit()



#### Querrying some data

#cursor.execute("SELECT * FROM tablename")
#cursor.fetchall()

# fetch methods
# fetchall -
# fetchone -    gets one row of the result
# fetchmany(number_rows) -   gets arbritary number of rows

#("select * from people WHERE email like '%.com'")
#("select * from people WHERE email like '%.com'")
#("select * from people WHERE last_name like 'Br%'")
#result = cursor.execute("select * from people")
#print(result.fetchall())

#result2 = cursor.execute("select * from people where name like :name", {"name": "bob"})
#print(result2.fetchall())

#result3 = cursor.execute("select count from people where name like :name", {"name": "jill"})
#print(result3.fetchall())

# rowid
#("select rowid, * from people WHERE email like '%.com'")


#### Formating Results

cursor.execute("SELECT * FROM tablename")

#print(c.fetchone()[0])

items = cursor.fetchall()
print(items)

# For convenience is possible to iterate over a cursor objects rows similarly to iterating over a file:
#item = cursor.execute("select * from people")
#for i in items:
#    print(i[0])
#    print(i)
#    print(i[0],i[1],i[2])



#### Modifying

#cursor.execute("update people set count=? where name=?", (20, "Jill"))
#cursor.execute("update people set name=? where name=?", ("notBob", "Bob"))

cursor.execute(""" UPDATE tablename 
               SET first_name = 'Robert',
               WHERE first_name = 'Bob'
               """)



#### Delete Records

cursor.execute(""" DELETE from tablename 
               WHERE rowid = 6
               """)




#### Order Records
cursor.execute(""" SELECT rowid, * FROM tablename
               ORDER BY rowid DESC 
               """) # BY first_name, last_name, email, etc... ASC(default) DESC



#### AND/OR
cursor.execute(""" SELECT * FROM tablename 
               WHERE first_name = 'Bob' AND last_name = 'Brown'
               """)

cursor.execute(""" SELECT * FROM tablename 
               WHERE first_name = 'Bob' OR last_name = 'Brown'
               """)



#### Limit

#### Delete a Table

cursor.execute("""
               DROP TABLE customers
               """)











conn.commit()
conn.close()
