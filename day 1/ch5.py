# -*- coding: utf-8 -*-
"""
Created on Wed May  8 01:43:59 2019

@author: Vijay
"""

random_number=int(input("enter any number between 1 to 10 which will be choose by computer"))
guess_number=int(input("enter the number guess by the player"))
tries=6
while (tries<=6):
    if(random_number==guess_number):
    print("player win and the computer lose")
    else:
    print("player has another chance to play") 
     tries=tries+1