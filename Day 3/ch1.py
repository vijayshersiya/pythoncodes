# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:04:55 2019

@author: Vijay
"""

#Code Challenge
 # Name: 
  #  generator
  #Filename: 
   # generator.py
  #Problem Statement:
   # This program accepts a sequence of comma separated numbers from user 
    #and generates a list and tuple with those numbers.  
  #Input: 
   # 2, 4, 7, 8, 9, 12
  #Output:
   # List : ['2', ' 4', ' 7', ' 8', ' 9', '12'] 
    #Tuple : ('2', ' 4', ' 7', ' 8', ' 9', '122')
  
x=input("enter the element with comma:").split(",")
list1=[]
tuple1=() 
for i in x:
 list1.append(i)
 tuple1=tuple(list1)
print(list1)
print(tuple1)
    
 

 