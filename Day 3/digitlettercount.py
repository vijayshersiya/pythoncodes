# -*- coding: utf-8 -*-
"""
Created on Thu May  9 22:12:46 2019

@author: Vijay
"""

#Code Challenge
 # Name: 
 #  Digit Letter Counter
  #Filename: 
   # digit_letter_counter.py
  #Problem Statement:
   # Write a Python program that accepts a string from User and calculate the number of digits and letters.
  #Hint:
   # Store the letters and Digits as keys in the dictionary  
  #Input: 
   # Python 3.2
  #Output:
   # Digits 2
    #Letters 6 
    dict={}
    str=input("enter the string to count digit and letters:")
    for i in str:
        dict[i]=dict.setdefault(str,0)+1
        print(digit,letters)
        
    