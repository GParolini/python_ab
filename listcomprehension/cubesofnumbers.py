#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 22:19:51 2019

@author: giudittaparolini
"""

lst = []
for x in range (1,11):
    lst.append(x**3)
print(lst)


print ("--------")

lst1 = []
lst1 = [x**3 for x in range (1,11)]
print(lst1)