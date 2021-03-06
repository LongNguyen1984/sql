# JOINING data from multiple tables
import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    
    c.execute("""SELECT population.city, population.population, regions.region
              FROM population, regions WHERE population.city = regions.city""")
    rows = c.fetchall()
    
    for r in rows:
        print(r[0], r[1], r[2])
        
    c.execute("""SELECT DISTINCT population.city, population.population,
              regions.region FROM population, regions WHERE 
              population.city = regions.city ORDER by population.city ASC""")
    rows = c.fetchall()
    
    for r in rows:
        print("City:" + r[0])
        print("Population:" + str(r[1]))
        print("Region: " + r[2])
        print("")
        