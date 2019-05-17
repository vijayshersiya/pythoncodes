# -*- coding: utf-8 -*-
"""
Created on Mon May 13 11:08:11 2019

@author: Vijay
"""

"""
Code Challenge
  Filename: 
    map1.py
  Problem Statement:
import random

names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

for i in range(len(names)):
    names[i] = random.choice(code_names)

print (names)

As you can see, this algorithm can potentially assign the same secret code name to multiple secret agents. 


Rewrite the above code using map and lambda.
"""
import random
names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']
y1=list(map(lambda x:random.choice(code_names),names))
print(y1)

  

