#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 22:09:56 2019

@author: giudittaparolini
"""

from functools import reduce

lst = [5,10,15,20]
result= reduce(lambda x,y: x+y, lst)
print(result)