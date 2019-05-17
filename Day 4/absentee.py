# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:06:28 2019

@author: Vijay
"""
# Code Challenge
 # Name: 
  #  Create a list of absentee
  #Filename: 
   # absentee.py
  #Problem Statement:
   # Make a program that create a file absentee.txt
    #The program should take max 25 students name one by one
    #When the user enter a blank line, it should terminate the input
    #Store all the name of students in the file    
        #Once all the students names have been entered, it should display the list
    count=0
    fp=open("absentee.txt","w")
    while(True):
      x=input("enter the name of student:")
      count=count+1
      fp.write(x)
      fp.write("\n")
      if not x or count == 26:
         break
    fp.close()
    with open("absentee.text",mode="rt") as fp:
      fp2=fp.read(x)    
      print(fp2)
   
    
       