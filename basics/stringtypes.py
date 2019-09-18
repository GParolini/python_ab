#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 11:45:03 2019

@author: giudittaparolini
"""

s="  You are awesome  "
print(s)

s1="""You are
the creator
of your destiny"""
print(s1)

#indexing
print(s[0])
print(s[2])

#repetition
print(s*2)
print(s*3)

#length
print(len(s1))
print(len(s))

#slicing 
print(s[0:5]) #without ending index
print(s[0:])
print(s[:8])
print(s[-3:-1]) #- for reverse order
print(s[0:9:2])
print(s[15::-1]) #reverse
print(s[::-1])

#strip white spaces
print(s.strip()) #strip white spaces
print(s.lstrip()) #strip white spaces on the left
print(s.rstrip()) #strip white spaces on the right

#find function
print(s.find("awe"), 0, len(s))
print(s.find("awe", 0, len(s)))
print(s.find("awe", 0, 8)) #returns -1 when it cannot find string

#count function
print(s.count("a"))

#replace function
print(s.replace("awesome", "super"))

#replace small case with upper case and vice versa
print(s.upper())
print(s.lower())
print(s.title())