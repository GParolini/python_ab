#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 22:25:03 2019

@author: giudittaparolini
"""

'''
#list comprension to show the even numbers from 0 to 20
lst = [x for x in range (2,21,2)]
print(lst)
'''

lst=[x for x in range(1,21) if x%2 ==0]

print(lst)