#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 08:44:32 2019

@author: giudittaparolini
"""
try:
    
    num = int(input ("Enter a even number:"))
    assert num%2==0, "You have entered a invalid input"

except AssertionError as obj:
    print(obj)
    
print ("After the assertion")