import sqlite3

conn = sqlite3.connect("../datafile.db")
cursor = conn.cursor()

# Some insert examples

#cursor.execute("create table people (id integer primary key, name text, count integer)")
#
#cursor.execute("insert into people (name,count) values ('Bob', 1)")
#
#cursor.execute("insert into people (name, count) values (?,?)", ("Jill", 15))
#
#cursor.execute("insert into people (name, count) values (:username, :usercount)", {"username": "Joe", "usercount":10})
#
#conn.commit()


# Querrying some data
#result = cursor.execute("select * from people")
#print(result.fetchall())
#
#result2 = cursor.execute("select * from people where name like :name", {"name": "bob"})
#print(result2.fetchall())
#
#result3 = cursor.execute("select count from people where name like :name", {"name": "jill"})
#print(result3.fetchall())


# Modifying
#cursor.execute("update people set count=? where name=?", (20, "Jill"))
#
cursor.execute("update people set name=? where name=?", ("notBob", "Bob"))
#
#result = cursor.execute("select * from people")
#print(result.fetchall())


# fetch methods
# fetchall -
# fetchone -    gets one row of the result
# fetchmany(number_rows) -   gets arbritary number of rows

#conn.commit() make changes permanent in the database as conn.close() doesn't autommatically commit any changes
conn.commit()

# For convenience is possible to iterate over a cursor objects rows similarly to iterating over a file:
result = cursor.execute("select * from people")
for row in result:
    print(row)

conn.close()
