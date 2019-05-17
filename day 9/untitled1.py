# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:43:01 2019

@author: Vijay
"""
"""
Code Challenge 2
Perform similar steps as in the above code challenge but store the contents in 
an online mongo atlas database
"""

import pymongo
#import dns # required for connecting with SRV
#client = pymongo.MongoClient("mongodb://K_Vaid:123chandu30%26@cluster0-shard-00-00-tofyu.mongodb.net:27017,cluster0-shard-00-01-tofyu.mongodb.net:27017,cluster0-shard-00-02-tofyu.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
client = pymongo.MongoClient("mongodb://vijay1997:vijay%401997@vijay-shard-00-00-obffw.gcp.mongodb.net:27017,vijay-shard-00-01-obffw.gcp.mongodb.net:27017,vijay-shard-00-02-obffw.gcp.mongodb.net:27017/test?ssl=true&replicaSet=vijay-shard-0&authSource=admin&retryWrites=true")

mydb = client.vijayshersiyadb

def add_stu(student_name,student_age,student_roll_no,student_branch):
    #unique_employee = mydb.employees.find_one({"id":idd})
    #if unique_employee:
    #    return "Employee already exists"
    #else:
    mydb.vijay.insert_one(
   {
     "student_name" :student_name ,
     "student_age" :student_age,  
     "student_roll_no" : student_roll_no, 
     "student_branch " :  student_branch
   })
    return "stu added successfully"


def fetch_all_stu():
    user = mydb.vijay.find()
    for i in user:
        print (i)

add_stu ('vijay',22, 45, 'cs')
add_stu ('mohit',21, 46, 'cs')
add_stu ('dig',23, 47, 'cs')
add_stu ('viku',24, 48, 'cs')
add_stu ('anupam',22, 49, 'cs')

fetch_all_stu()