#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 15:37:51 2019

@author: giudittaparolini
"""

#duck typing

class Duck:
    def talk(self):
        print("Quack Quack")
    
class Human:
    def talk(self):
        print("Hello") 

def callTalk(obj):
    obj.talk();
    
d=Duck()
callTalk(d)

h= Human()
callTalk(h)