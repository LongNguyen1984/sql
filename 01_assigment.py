# Create a SQLite3 database and table
# import the sqlite3 library
import sqlite3

# create a new database if the database doesn't already exist
#conn = sqlite3.connect("car.db")

# get a cursor object used to execute SQL commands
#cursor = conn.cursor()

"""Make 5 data into a table of car.db
vehicles = [
    ('Fords', 'Standar', 60000),
    ('Fords', 'Lux', 27000),
    ('Fords', 'Lux', 21000),
    ('Hondas', 'Sport', 15000),
    ('Hondas', 'Standar', 75000)
]
# insert data into table
cursor.executemany('INSERT INTO inventory VALUES(?, ?, ?)', vehicles)
"""
with sqlite3.connect("car.db") as connection:
    c = connection.cursor()
    
    #update data
    c.execute("UPDATE inventory SET quantity = 78000 WHERE Make='Fords' AND Model ='Standar'")
    c.execute("UPDATE inventory SET quantity = 18000 WHERE Make='Hondas' AND Model ='Standar'")
    # delete data
    #c.execute("DELETE FROM population WHERE city='Boston'")
    
    print("\nNEW DATA:\n")
    # output all data
    c.execute("SELECT * FROM inventory")
    
    rows = c.fetchall()
    
    for r in rows:
        print(r[0], r[1], r[2])
# Output only records that are for Fords vehicles
    print("\n Information from Fords inc.:\n")
    c.execute("SELECT * FROM inventory WHERE Make = 'Fords'")
    
    rows = c.fetchall()
    
    for r in rows:
        print(r[1], r[2])
# commit the change
#conn.commit()
#close the database connection
#conn.close()