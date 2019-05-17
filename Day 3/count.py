# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:58:22 2019

@author: Vijay
"""

 #Character Frequency
  #Filename: 
   # frequency.py
  #Problem Statement:
   # This program accepts a string from User and counts the number of characters (character frequency) in the input string.  
  #Input: 
   # www.google.com
  #Output:
   # {'c': 1, 'e': 1, 'g': 2, 'm': 1, 'l': 1, 'o': 3, '.': 2, 'w': 3
 dict={}
 str=input("enter the string to check no of character:")
 for char in str:
     if char not in dict.keys():
         dict[char]=1
     else:
         dict[char]=char+1