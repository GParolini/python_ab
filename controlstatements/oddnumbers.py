#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 16:31:47 2019

@author: giudittaparolini
"""

x = int(input("Enter min number"))

y = int(input("Enter max number"))

i = x
if i%2 == 0: i = i+1
while i<=y:
    print (i)
    i+=2