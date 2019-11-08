#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 18:01:20 2019

@author: giudittaparolini
"""

from threading import *
from time import sleep

class MyThread:
    def displayNumbers(self):
        i = 0
        print(current_thread().getName())
        sleep(1)
        while (i<=10):
            print(i)
            i+=1

obj = MyThread()
t1 = Thread(target=obj.displayNumbers)
t1.start()

t2 = Thread(target=obj.displayNumbers)
t2.start()

t3 = Thread(target=obj.displayNumbers)
t3.start()