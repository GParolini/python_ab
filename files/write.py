#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 23:05:13 2019

@author: giudittaparolini
"""
#opens the file for writing
f = open("myfile.txt", "w")
s = input("Enter text: ")
f.write(s)
f.close()


