# -*- coding: utf-8 -*-
"""
Created on Thu May  9 00:40:31 2019

@author: Vijay
"""





  #  Write following functions for list operations. Take list as input from the User
   # Add(), Multiply(), Largest(), Smallest(), Sorting(), Remove_Duplicates(), Print()
    #Only call Print() function to display the results in the below displayed 
    #format (i.e all the functions must be called inside the print() function 
    #and only the Print() is to be called in the main script)

  #Input: 
   # 5,2,6,2,3
  #Output:
   # Sum = 18
    #Multiply = 360
   # Largest = 6
    #Smallest = 2
    #Sorted = [2, 2, 3, 5, 6]
    #Without Duplicates = [2, 3, 5, 6]
    
    
i=0
sum=0 
mul=1   
list=[1,2,3,4,5,6]
for i in range(1,5):
    sum=sum+list[i]
    print("sum",sum)
    mul=mul*list[i]
    print("mul",mul)
    list.largest()
    
 