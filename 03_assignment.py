import sqlite3

with sqlite3.connect("car.db") as connection:
    c = connection.cursor()
    
    # create a dictionary of sql queries
    sql = {'average:': "SELECT avg(quantity) FROM inventory",
           'maximum' : "SELECT max(quantity) FROM inventory",
           'minimum' : "SELECT min(quantity) FROM inventory",
           'sum': "SELECT sum(quantity) FROM inventory",
           'count': "SELECT count(quantity) FROM inventory"}
    
    # run each sql query item in the dictionary
    for keys, values in sql.items():
        # run sql
        c.execute(values)
        
        # fetchone() retrives one record from the query
        result = c.fetchone()
        
        #output the result to screen
        print(keys + ":", result[0])
        