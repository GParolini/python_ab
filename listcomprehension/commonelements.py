#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 22:31:24 2019

@author: giudittaparolini
"""

a= [2,4,6,8]
b = [1,2,3,4]

'''
result=[]
for i in a:
    if i in b:
        result.append(i)
print(result)

'''

result = []
result = [i for i in a if i in b]
print(result)