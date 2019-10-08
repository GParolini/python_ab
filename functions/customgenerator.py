#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 22:06:46 2019

@author: giudittaparolini
"""

def customgen(x,y):
    while x<y:
        yield x
        x+=1
        
result = customgen(20,30)

for i in result:
    print(i)