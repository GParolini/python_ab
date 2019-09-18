#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 14:26:39 2019

@author: giudittaparolini
"""

s={10,20,30,"XYZ"}
print(s)
print(type(s))

s1={10,20,30,"XYZ",10,20,10}
print(s1) #duplicates are not taken into account

#add element to a set
s.update([88,99]) #no order
print(s)
print(type(s))

#no indexing, slicing or repetition
#print(s[0])#results in an error
#print(s[0:5])#results in an error
#print(s*3)#results in an error

#remove
s.remove(30)
print(s)

#transform the set in a frozen set. You cannot perform update and delete on a frozen set
f=frozenset(s)
#f.update([20]) throws an error, same with remove
