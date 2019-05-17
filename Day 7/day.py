# -*- coding: utf-8 -*-
"""
Created on Tue May 14 21:12:11 2019

@author: Vijay
"""

"""
# Make a function days_in_month to return the number of days in a specific month of a year
"""
list1=['jan','mar','may','jul' ,'aug','oct','dec']
list3=['feb']
list2=['apr','jun','sep','nov']
def days_in_month(x,y):
  if x in list1 or (y%4 == 0 and y%100!=0) or y % 400 == 0:
     return 31
  elif x in list2 or (y%4 == 0 and y%100!=0) or y % 400 == 0:
     return 30 
  elif x in list3 and (y%4 == 0 and y%100!=0) or y % 400 == 0:
      return 28
  elif x in list3 and not(y%4 == 0 and y%100!=0) or y % 400 == 0:
      return 29
x=input("enter the month name to find the no of days:")
y=int(input("enter the year to check no of days in month:"))
days_in_month(x,y)