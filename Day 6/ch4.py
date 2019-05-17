# -*- coding: utf-8 -*-
"""
Created on Mon May 13 11:54:07 2019

@author: Vijay
"""
"""
Code Challenge
  Filename: 
    height.py
  Problem Statement:

people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

height_total = 0
height_count = 0
for person in people:
    if 'height' in person:
        height_total += person['height']
        height_count += 1

if height_count > 0:
    average_height = height_total / height_count

    print (average_height)
    
Try rewriting the code below using map, reduce and filter. 
Filter takes a function and a collection. 
It returns a collection of every item for which the function returned True.
"""
people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]
 
def cal_height(height):
     sum1=list(map(lambda x:cal_height(height),people))
     sum2=list(map(lambda x:average_height(height),people))
print(sum1)
print(sum2)



        
