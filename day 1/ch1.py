# -*- coding: utf-8 -*-
"""
Created on Wed May  8 01:06:43 2019

@author: Vijay
"""

random_number=int(input("enter any number between 1 to 10 which will be choose by computer"))
guess_number=int(input("enter the number guess by the player"))
if(random_number==guess_number):
    print("player win and the computer lose")
else:
    print("player lose and the computer wins")
    print("secret_number {} ".format("random_number")
