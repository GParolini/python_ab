#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 23:04:03 2019

@author: giudittaparolini
"""

#factorial


def factorial (n):
    if n == 0:
        result = 1
    else:
        result = n*factorial(n-1)
    return result

print(factorial(5))
print(factorial(6))