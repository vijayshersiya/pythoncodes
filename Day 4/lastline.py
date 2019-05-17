# -*- coding: utf-8 -*-
"""
Created on Sat May 11 03:13:14 2019

@author: Vijay
"""
"""
Code Challenge
  Name: 
    Last Line
  Filename: 
    lastline.py
  Problem Statement:
    Ask the user for the name of a text file. 
    Display the final line of that file.
    Think of ways in which you can solve this problem, 
    and how it might relate to your daily work with Python
    """
fp=open("words.txt","rt")
fp2=fp.read()
fp.close()
with open("vijay3.txt","w")as fp3:
fp3.write(fp2)
read1=fp3.readlines()
print(read1)
fp3.seek(-5,2)

