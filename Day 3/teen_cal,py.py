# -*- coding: utf-8 -*-
"""
Created on Thu May  9 22:19:27 2019

@author: Vijay
"""

#Code Challenge
 # Name: 
  #  Teen Calculator
  #Filename: 
   # teen_cal.py
  #Problem Statement:
   # Take dictionary as input from user with keys, a b c, with some integer 
    #values and print their sum. However, if any of the values is a teen -- 
    #in the range 13 to 19 inclusive -- then that value counts as 0, except 
    #15 and 16 do not count as a teens. Write a separate helper "def 
    #fix_teen(n):"that takes in an int value and returns that value fixed for
    #the teen rule. In this way, you avoid repeating the teen code 3 times  
  #Input: 
   # {"a" : 2, "b" : 15, "c" : 13}
  #Output:
   # Sum 
   d={}
   n=4
   x=[map(int,raw_input().split()) for x in range(n)
    def fix_teen(n):
        if d in range(13,20):
          return sum=0
        elif d in range(15,16):
            return sum+d
    fix_teen(4)