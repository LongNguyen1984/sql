import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    """
    # use a for loop to iterate through the database, printing the results line by line
    for row in c.execute("SELECT firstname, lastname from employees"):
        print(row)
    """
    c.execute("SELECT firstname, lastname from employees")
    
    rows= c.fetchall()
    
    for r in rows:
        print(r[0], r[1])