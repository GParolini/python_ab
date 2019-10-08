#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 22:04:40 2019

@author: giudittaparolini
"""

lst = [10, 2, 33, 45, 89, 2]

result = list(filter (lambda x: x%2==0, lst))
print(result)

for i in result: print(i)