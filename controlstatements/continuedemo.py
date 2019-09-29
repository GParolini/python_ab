#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 17:04:30 2019

@author: giudittaparolini
"""
#with continue you skip 
x = 0
while x<20:
    x +=1
    if x%3 == 0:
        continue
    print(x)