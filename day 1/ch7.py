# -*- coding: utf-8 -*-
"""
Created on Wed May  8 01:58:39 2019

@author: Vijay
"""

 tries=8
random_number=int(input("enter any number between 1 to 10 which will be choose by computer"))
guess_number=int(input("enter the number guess by the player"))
while (tries<=8):
    if(random_number==guess_number):
     print("player win and the computer lose")
    else:
     print("player has another chance to play")
     tries=tries-1