#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 16:51:39 2019

@author: giudittaparolini
"""

#Multiplication table

x =int(input("Enter a number for generating a multiplication table"))

for i in range (1,11):
    print (x, "X", i, '=', i*x)