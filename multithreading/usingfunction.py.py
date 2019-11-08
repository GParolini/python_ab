#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 17:50:15 2019

@author: giudittaparolini
"""

from threading import *

def displayNumbers():
    i = 0
    print(current_thread().getName())
    while (i<=10):
        print(i)
        i+=1


print(current_thread().getName())

t = Thread(target=displayNumbers)

t.start()