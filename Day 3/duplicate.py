# -*- coding: utf-8 -*-
"""
Created on Thu May  9 22:19:26 2019

@author: Vijay
"""

#Code Challenge
 # Name: 
  #  Duplicate
  #Filename: 
   # duplicate.py
  #Problem Statement:
   # With a given list [12,24,35,24,88,120,155,88,120,155]
    #Write a program to print this list after removing all duplicate values 
    #with original order reserved 
# Code Challenge
 # Name: 
  #  Duplicate
  #Filename: 
   # duplicate.py
  #Problem Statement:
   # With a given list [12,24,35,24,88,120,155,88,120,155]
    #Write a program to print this list after removing all duplicate values 
   # with original order reserved 
list1=[12,24,35,24,88,120,155,88,120,155]
list2=[]
for i in list1:
   if i not in list2:
      list2.append(i)
print(list2)
           