#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 18:55:42 2019

@author: giudittaparolini
"""

c=["Italy", "Germany", "USA"]
print(c)

print ("-----")

c.append("Spain")
print(c)

print ("-----")

c.remove(c[2])
print(c)

print ("-----")

c.insert(2,"Switzerland")
print(c)

print ("-----")
print ("-----")


s={"Austria", "UK", "Poland" }
print(s)
print(type(s))

print ("-----")

s.add("Netherlands")
print(s)

print ("-----")
s.remove("Poland")
print(s)

#It is not possible to insert an element at a specific place in a set
s.add("Russia")
print(s)