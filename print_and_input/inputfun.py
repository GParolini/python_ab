#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 22:42:27 2019

@author: giudittaparolini
"""

'''
#when the input function is used the execution of the code stops until the user gives an input
s=input()
print(s)

s=input("Enter your first name")
print(s)
'''

'''
i=int(input("Enter an integer number"))
print(i)
print(type(i))
'''

#input("Enter three numbers separated by a space:").split('')

'''
lst = [x for x in input("Enter three numbers separated by a space:").split()]
print(lst)
'''

lst1 = [x for x in input("Enter three numbers separated by a comma:").split(',')]
print(lst1)