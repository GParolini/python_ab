#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 23:03:40 2019

@author: giudittaparolini
"""

tpl=()
print(tpl)

tpl1=(40,50,40, "XYZ")
print(tpl1)

tpl2=(40,) #always add the comma for tuples with a single element
print(tpl2)
print(type(tpl2))

#call a tuple element
print(tpl1[3])

#repeat
print(tpl1*3)

#count
print(tpl1.count(40))

#find the index of an element
print(tpl1.index("XYZ"))

lst=[67,34,"XYZ"]
print(type(lst))
tpl_lst= tuple(lst)
print(type(tpl_lst))
print(tpl_lst)
