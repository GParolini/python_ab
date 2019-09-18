#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 18:42:40 2019

@author: giudittaparolini
"""

lst=[20,30,40,235]#max value fpr a byte 255
print(type(lst))

b=bytes(lst)
print(type(b))

#you cannot add elements to a byte, slice or repeate
#b[3]=22

b1=bytearray(lst)
print(type(b1))

#you can modify a bytearray
b1[2]=33
