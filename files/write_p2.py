#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 23:10:40 2019

@author: giudittaparolini
"""

#write multiple lines
f1 = open("myfile1.txt", "w")
print("Enter text (Type # when you are done)")

s = " "
while s != "#":                
    s = input()
    f1.write(s + "\n")

f1.close()