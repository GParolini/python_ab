#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 00:15:35 2019

@author: giudittaparolini
"""

a=b=c=10
print(a,b,c)

x,y=10,5
x+=y
print(x)

x*=y #75 because now x is not 5, but 15 (see passage above)
print(x)

x-=y #(75-5)
print(x)

x%=y #70/5=14 
print(x)

x//=y #0/5 =0
print(x)