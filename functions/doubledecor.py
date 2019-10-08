#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 22:13:30 2019

@author: giudittaparolini
"""

def decorfun(fun):
    def inner():
        result = fun()
        return result*2
    return inner


@decorfun #the decorator function will be automatically applied to all the functions listed below
def num():
    return 5

#resultfun = decor(num)
#print(resultfun())
    
print(num())