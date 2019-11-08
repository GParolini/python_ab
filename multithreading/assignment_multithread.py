#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 09:03:33 2019

@author: giudittaparolini
"""

from threading import *
from time import *

class EvenNumbers:
    def __init__(self):
        self.l = Lock()
    def printE (self):
        self.l.acquire()
        for i in range(0,101):
            if i % 2 ==0:
                print(i)
        self.l.release()

class OddNumbers:
    def __init__(self):
        self.l = Lock()
    def printO(self):
        self.l.acquire()
        for i in range(0,101):
            if i % 2 !=0:
                print(i)
        self.l.release()
        
class Main:
    def __init__(self):
        self.l = Lock()
    def printAll (self):
        self.l.acquire()
        for i in range(0,101):
            print(i)
        self.l.release()   
        
        

e = EvenNumbers()
o = OddNumbers()
m = Main()

t1 = Thread(target= e.printE)
t2 = Thread(target= o.printO)
t3 = Thread(target= m.printAll)

t1.start()
t1.join()
t2.start()
t2.join()
t3.start()