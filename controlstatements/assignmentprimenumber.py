#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 17:39:53 2019

@author: giudittaparolini
"""

x = int(input("Please, enter a number: "))

lst = []

for i in range (2,x):
    if x%i == 0:
        lst.append(i)
    else:
        continue


if x == 1:
    print ("1 is not a prime number")
else:
    print("The divisors of", x, "are: 1 and", lst)

if (len(lst) == 0) & (x != 1):   
    print (x, "is a prime number")
else:
    if x != 1:
        print (x, "is not a prime number") 

