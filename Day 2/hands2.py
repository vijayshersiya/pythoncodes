# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:23:52 2019

@author: Vijay
"""
#Hands On 2
#Make a function to find whether a year is a leap year or no, return True or False



def check_leapyear(x):
    if (x%4 == 0 and x%100 != 0) or x % 400 == 0:
        return True
    else:
        return False

x=int(input("enter the year to check it is leap or not:"))
check_leapyear(x)