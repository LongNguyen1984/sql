# Create a SQLite3 database and table
# import the sqlite3 library
import sqlite3

with sqlite3.connect("car.db") as connection:
    c = connection.cursor()
    
    # insert multiple records using a tuple
    # (you can copy and paste the values)
    
        
    # create a new table
    try:
        c.execute("""CREATE TABLE orders
              (make TEXT, model TEXT, order_date DATE)
              """)
    except:
        pass
    # data
    order = [
('Fords', 'Standar', '2016-01-01'),
('Fords', 'Standar', '2015-11-01'),
('Fords', 'Lux', '2016-01-21'),
('Fords', 'Standar', '2016-07-01'),
('Fords', 'Standar', '2018-09-13'),
('Hondas', 'Standar', '2017-03-03'),
('Fords', 'Standar', '2015-12-31'),
('Fords', 'Standar', '2019-05-06'),
('Hondas', 'Standar', '2019-05-12'),
('Fords', 'Standar', '2020-10-12'),
('Fords', 'Lux', '2021-11-31'),
('Fords', 'Standar', '2016-04-15'),
('Hondas', 'Sport', '2018-07-24'),
('Hondas', 'Standar', '2019-08-08'),
('Fords', 'Standar', '2021-03-031'),
('Hondas', 'Sport', '2021-12-20'),
('Fords', 'Lux', '2022-01-09'),
('Hondas', 'Standar', '2022-05-13')

]
    c.executemany("INSERT INTO orders VALUES(?, ?, ?)", order)
    
    c.execute("SELECT * FROM orders ORDER BY order_date ASC")
    
    rows = c.fetchall()
    
    for r in rows:
        print(r[0], r[1], r[2])
        
