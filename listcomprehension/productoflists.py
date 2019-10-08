#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 22:27:52 2019

@author: giudittaparolini
"""

a = [1,2,3,4,5]
b = [6,7,8,9,10]

'''
z = []

for i in range (len(a)):
    z.append(a[i]*b[i])
print(z)

'''

z = []
z = [a[i]*b[i] for i in range(len(a))]
print (z)