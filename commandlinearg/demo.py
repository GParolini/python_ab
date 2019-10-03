#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 20:15:09 2019

@author: giudittaparolini
"""

import sys #import the module that stores command line arguments. File name is the first command line argument by default

lst=sys.argv 

for i in lst:
    print(i)

print(len(lst))

print(lst[0])
