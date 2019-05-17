# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:34:08 2019

@author: Vijay
"""
list1=[]
x=input("enter the value:" ).split(",")  
list1.append(x)
print(list1)
list1=[]
for x in range(4):
  list1.append(input("enter the value:",x+1))
  print(list1)
  