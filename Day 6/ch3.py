# -*- coding: utf-8 -*-
"""
Created on Mon May 13 11:54:06 2019

@author: Vijay
"""
"""
Code Challenge
  Filename: 
    map2.py
  Problem Statement:

names = ['Mary', 'Isla', 'Sam']

for i in range(len(names)):
    names[i] = hash(names[i])

print (names)



(Hopefully, the secret agents will have good memories and won’t forget each other’s secret code names during the secret mission.)


Rewrite the above code using map.
"""
names=['Mary', 'Isla', 'Sam']
y2=list(map(lambda x:hash(x),names))
print(y2)
 
 
   
     
    
