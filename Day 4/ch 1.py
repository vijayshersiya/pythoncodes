# -*- coding: utf-8 -*-
"""
Created on Fri May 10 09:16:13 2019

@author: Vijay
"""
#Code Challenge
 # Name: 
  #  copy command
  #Filename: 
   # copy.py
 #Problem Statement:
# Make a program that create a copy of a file

fp = open("words.txt", "r")
fp2=fp.read()
fp.close()
fp3=open("vijay1.txt","w")
fp3.write(fp2)
fp3.close()