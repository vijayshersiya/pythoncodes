# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:26:32 2019

@author: Vijay
"""
"""
Code Challenge 1
Write a python code to insert records to a mongo/sqlite/MySQL database 
named db_University for 10 students with fields like 

Student_Name, Student_Age, Student_Roll_no, Student_Branch.
"""


import os
import sqlite3
from pandas import DataFrame
conn = sqlite3.connect ( 'db_university.db' )
c = conn.cursor()
c.execute ("""CREATE TABLE student(
          student_name TEXT,
          student_age INTEGER,
          student_roll_no INTEGER,
          student_branch TEXT
          )""")
c.execute("INSERT INTO student VALUES ('vijay',22, 45, 'cs')")
c.execute("INSERT INTO student VALUES ('mohit',21, 46, 'cs')")
c.execute("INSERT INTO  student VALUES ('dig',23, 47, 'cs')")
c.execute("INSERT INTO  student VALUES ('viku',24, 48, 'cs')")
c.execute("INSERT INTO  student VALUES ('anupam',22, 49, 'cs')")
c.execute("SELECT * FROM student")
# "SELECT * FROM employees WHERE last = 'Fernandes' "
print ( c.fetchone())
# STEP 4
# returns one or otherwise None as a tuple
print ( c.fetchone()) 

# returns one or otherwise None as a tuple
print ( c.fetchmany(2)) 

# returns a list of tuples
print ( c.fetchall() )


# Since now the cursor has read all the rows and we are at End
# So again fetching the records from the database
c.execute("SELECT * FROM student")


# STEP 5
df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["student_name","student_age","student_roll_no","student_branch"]


# STEP 6
# commits the current transaction 
conn.commit()

# STEP 7
# closing the connection 
conn.close()