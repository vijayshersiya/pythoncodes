# -*- coding: utf-8 -*-
"""
Created on Wed May  8 21:36:33 2019

@author: Vijay
"""

#Hands On 3
 
#Make a function days_in_month to return the number of days in a specific month of a year
year=int(input("enter the year:"))
month=[january,february,march,april,may,june,july,august,september,october,november, december]
if(month==january or month==march ) or (month== may or month==july):
 print("31 day in a month of year",year)
elif(month==august or months==october) or month==december:
 print("31 days in a months of year",year)
else:
 print("30 days in a monthd==s of year",year)
 
 
             