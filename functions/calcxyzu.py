#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 22:31:54 2019

@author: giudittaparolini
"""

def calc(a,b):
    x = a+b
    y = a-b
    z= a*b
    u= a/b
    return x,y,z,u

result = calc(10,5)
print (result)

for i in result:
    print(i)