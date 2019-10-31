#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 23:08:50 2019

@author: giudittaparolini
"""
import os
import sys

if os.path.isfile("myfile123.txt"):
    f = open("myfile.txt", "r")
   
else:
    print("File does not exist")
    sys.exit()

s = f.read()
print(s)
f.close()

print ("-------------")

f1 = open("myfile1.txt", "r")
s1 = f1.read()
print(s1)
f1.close()