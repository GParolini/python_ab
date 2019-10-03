#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 22:21:10 2019

@author: giudittaparolini
"""

"""
def average(a,b):
    print("average of the two given numbers is", (a+b)/2)
    
average(10,20)

"""
'''
def average(a,b):
    print(a)
    print(b)
    return (a+b)/2
    
c = average(10,20)
print(c)
print (average(b=10,a=20))

'''

def average(a=10,b=20): #a,b, are default values
    print(a)
    print(b)
    return (a+b)/2
    

print (average(a=30))