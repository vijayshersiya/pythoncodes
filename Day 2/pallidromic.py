# -*- coding: utf-8 -*-
"""
Created on Wed May  8 12:41:36 2019

@author: Vijay
"""

  #Name: 
   # Pallindromic Integer
  #Filename: 
   # pallindromic.py
  #Problem Statement:
   # You are given a space separated list of integers. 
    #If all the integers are positive and if any integer is a palindromic integer, 
    #then you need to print True else print False.
    #(Take Input from User)  
  #Hint: 
   #   A palindromic number or numeral palindrome is a number that remains the same
    #  when its digits are reversed. 
     # Like 16461, for example, it is "symmetrical"
      #Shorter logic can be developed using any and all and List comprehension


i=0
num=1
reverse=0
list=[232,111,234,236]
print(list)
for i in range(0,4):
 while(list[i]!=0):
  list[i]=list[i]%10
  reverse=reverse*10+list[i]
  list[i]=list[i]/10
  if(reverse==list[i]):
   print("number is palidrome")
   i=i+1
  else:
   print("number is not palidrome")
   i=i+1
   list[i]=list[i]+1


 