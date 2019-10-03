#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 22:31:46 2019

@author: giudittaparolini
"""
'''
x = 123 #global variable

def display():
    y = 678
    print(x) #here I can still access x, because it is a global variable
    print(globals()['x'])


print(x)
print(y) #local variable. Local variable defined in a function take precedence over global variables within that function

'''

x = 123 #global variable

def display():
    x = 678
    print(x)
    print(globals()['x'])


print(x)
z = display
z()