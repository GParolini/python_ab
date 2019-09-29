#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 17:13:18 2019

@author: giudittaparolini
"""
"""
x = int(input("Please, enter a number"))

for i in range(x+1):
    if i%10 == 0:
        continue
    if i> 100:
        break 
    print(i)
"""    
   
#modified exercise that accepts also a float input
    
x = input("Please, enter a number")

y = float(x)
z = int(y)

for i in range(z+1):
    if i%10 == 0:
        continue
    if i> 100:
        break 
    print(i)
    