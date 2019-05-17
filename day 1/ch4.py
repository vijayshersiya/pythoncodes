# -*- coding: utf-8 -*-
"""
Created on Wed May  8 01:36:24 2019

@author: Vijay
"""

random_number=int(input("enter any number between 1 to 10 which will be choose by computer"))
guess_number=int(input("enter the number guess by the player"))
while(random_number<11):
    if(random_number==guess_number):
    print("player has been won match")
    else:
    print("player has another chance to play") 
    random_number=random_number+1