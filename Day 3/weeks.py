# -*- coding: utf-8 -*-
"""
Created on Thu May  9 22:19:28 2019

@author: Vijay
"""

# Code Challenge
 # Name: 
  #  weeks
  #Filename: 
   # weeks.py
  #Problem Statement:
   # Write a program that adds missing days to existing tuple of days
  #Input: 
   # ('Monday', 'Wednesday', 'Thursday', 'Saturday')
  #Output:
   # ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
str=('mon','tue','wed','thu','fri','sat','sun')
str1=('mon','wed','thu','sat')
tuple2=()
for i in str:
  for j in str1:
      if str[i]==str1[j]:
          i=i+1
      elif str[i]!==str1[j]:
          tuple2=tuple1.append(i)
          i=i+1