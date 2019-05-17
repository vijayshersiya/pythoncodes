# -*- coding: utf-8 -*-
"""
Created on Tue May 14 22:42:42 2019

@author: Vijay
"""

"""
Code Challenge
  Name: 
    Vowels Finder
  Filename: 
    vowels.py
  Problem Statement:
    Remove all the vowels from the list of states  
  Hint: 
    Use nested for loops and while
  Input:
    state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
  Output:
    ['lbm', 'clfrn', 'klhm', 'flrd']
    """
list1=[]
state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
vowels = ('a','e','i','o','u')
for i in state_name:
  for element in vowels:
     while element in state_name:
        new=state_name.remove(element)
        list1.append(new)
print(list1)
         
