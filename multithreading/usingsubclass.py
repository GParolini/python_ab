#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 17:54:29 2019

@author: giudittaparolini
"""

from threading import *

class MyThread(Thread):
    def run(self):
         i = 0
         while (i<=10):
             print(i)
             i+=1

t= MyThread()
t.start()