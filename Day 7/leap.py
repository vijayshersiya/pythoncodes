# -*- coding: utf-8 -*-
"""
Created on Tue May 14 20:56:27 2019

@author: Vijay
"""

"""
# Make a function to find whether a year is a leap year or no, return True or False
"""
def leap_year(x):
   if (x%4 == 0 and x%100 !=0) or x%400 == 0:
        return True
   else:
        return  
x=int(input("enter the year to check enter year is leap or not:"))
leap_year(x)