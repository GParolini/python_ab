#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 08:20:56 2019

@author: giudittaparolini
"""

try:

    a, b = [int(x) for x in input("Enter two numbers: ").split()]
    c = a/b 
    print(c)
    

except ZeroDivisionError:
    print("Division by zero is not allowed")
    print("Please enter a non zero numbers")

print("Code after the exception")