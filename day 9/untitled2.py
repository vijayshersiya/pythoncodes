# -*- coding: utf-8 -*-
"""
Created on Thu May 16 12:18:33 2019

@author: Vijay
"""
"""
Code Challenge 3
In the Bid plus Code Challenege 

          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)

Store the information into a database mySQL Database
"""
import mysql.connector 
# connect to  MySQL server along with Database name

conn = mysql.connector.connect(user='vijayshersiya', password='vijay@1997',
                              host='db4free.net', database = 'vijayshersiyadb')
#, database = 'forsk_test'

# creating cursor
c = conn.cursor()

# STEP 0
#c.execute("DROP DATABASE employee;")

# STEP 1
#c.execute("CREATE DATABASE employee;")

# STEP 2
c.execute("DROP Table ;")

# STEP 3
c.execute ("""CREATE TABLE employees(
          id INTEGER,
          first  TEXT,
          last TEXT,
          pay INTEGER
          )""")


# STEP 4
c.execute("INSERT INTO employees VALUES (01,'Sylvester', 'Fernandes', 50000)")
c.execute("INSERT INTO employees VALUES (02,'Yogendra', 'Singh', 70000)")
c.execute("INSERT INTO employees VALUES (03,'Rohit', 'Mishra', 30000)")
c.execute("INSERT INTO employees VALUES (04,'Kunal', 'Vaid', 30000)")
c.execute("INSERT INTO employees VALUES (05,'Devendra', 'Shekhawat', 30000)")

# c.execute("INSERT INTO employee VALUES ({},'{}', '{}', {})".format(idd, first,last,pay))


c.execute("SELECT * FROM employees")


# STEP 5
# returns one or otherwise None as a tuple
print ( c.fetchone()) 

# returns one or otherwise None as a tuple
print ( c.fetchmany(2)) 

# returns a list of tuples
print ( c.fetchall() )


# Since now the cursor has read all the rows and we are at End
# So again fetching the records from the database
c.execute("SELECT * FROM employees")


# STEP 6
df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["id","first","last","pay"]