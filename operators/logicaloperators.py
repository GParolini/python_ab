#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 08:57:05 2019

@author: giudittaparolini
"""

"""
X and Y (for boolean expressions). True is both True
X or Y True if one true
not X True if X false

"""

x=20
y=30

print((x==20 and y==30))#both true

print((x==25 and y==30))#x false

print((x==25 or y==30))#y is true

print((x==25 and y==31))#both false

print(not(x==25 and y==31))#due to the not