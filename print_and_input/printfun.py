#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 10:07:37 2019

@author: giudittaparolini
"""

print()

print("Hello " *3)

print("All the power is within you")
print("All the power \n is within you")

a,b=10,20
print(a,b)
print(a,b,sep=",")
print(a,b,sep="++++")

name="john"
marks="94.5"

print(name, marks)
print("Name is", name, "Marks are", marks)

marks=94.5678
print("Name is %s, Marks are %.2f" %(name, marks))
print("Name is %s, Marks are %.3f" %(name, marks))

print("Name is {}, Marks are {}".format(name, marks)) #format(*args, **kwargs)
print("Name is {}, Marks are {}".format(name, marks))