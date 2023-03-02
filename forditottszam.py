# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 20:38:44 2021

@author: Attila
"""
 
number = int(input("Adjon meg egy egész számot: "))  
  
revs_number = 0  
   
  
while (number > 0):   
    remainder = number % 10  
    revs_number = (revs_number * 10) + remainder  
    number = number // 10  
  
print("A fordított szám: {}".format(revs_number))  