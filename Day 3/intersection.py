# -*- coding: utf-8 -*-
"""
Created on Thu May  9 22:19:25 2019

@author: Vijay
"""

#Code Challenge
 # Name: 
  #  Intersection
  #Filename: 
  #  Intersection.py
  #Problem Statement:
  #  With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155]
  
  
  #  Write a program to make a list whose elements are intersection of the above given lists. 
list1=[]
list2=[]
x=input("enter the  element  with comma:").split(",") 
for i in x:
 list1.append(i)
y=input("enter the   element  with comma:").split(",")
for j in y:
 list2.append(j)
list3 =set(list1).intersection(set(list2))
print(list3)