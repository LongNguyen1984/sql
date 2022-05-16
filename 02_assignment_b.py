import sqlite3

with sqlite3.connect("car.db") as connection:
    c = connection.cursor()
    
    c.execute("""SELECT DISTINCT orders.make, orders.model, inventory.quantity, orders.order_date
              FROM orders, inventory WHERE
              orders.make = inventory.make AND orders.model = inventory.model 
              ORDER by orders.order_date ASC""")
    
    rows = c.fetchall()
    
    for r in rows:
        print("Make: " + r[0] + "- Model: " + r[1])
        print("Quantity: " + str(r[2]))
        print("Order date: " + r[3] )
        print("")