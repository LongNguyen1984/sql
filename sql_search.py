import sqlite3
import random

# 1. connect to the database
# 2. Establish a cursor.
# 3. Using a inf. loop to ask the user
    # 1. Calculate AVG
    # 2. Calculate MAX
    # 3. Calculate MIN
    # 4. Calculate SUM
    # 5. Break
    
# connect to the database
with sqlite3.connect("newnum.db") as connection:
    # Establish a cursor
    c = connection.cursor()
    print("Database is connected ...")
    # create a dictionary of sql queries
    sql = {'average:': "SELECT avg(num) FROM numbers",
           'maximum' : "SELECT max(num) FROM numbers",
           'minimum' : "SELECT min(num) FROM numbers",
           'sum': "SELECT sum(num) FROM numbers"}
    
    while True:
        print("Select a key to do action on the database!")
        print("Select 1-AVG, 2-MAX, 3-Min, 4-Sum and 5-Exit")
        key = input("Enter your number:")
        try: 
            key = int(key)
            #print(type(key1))
            if key <5 and key >0:
                c.execute(list(sql.values())[key-1])
                # fetchone() retrives one record from the query
                result = c.fetchone()
                #output the result to screen
                print(list(sql.keys())[key-1] + ":", result[0])
                
            elif key == 5:
                print('Exit program')
                break
            else:
                print('The key is out of range!!!')
                
        except ValueError:
            print('The key is not a number in range of 1-5')
            print("")
        