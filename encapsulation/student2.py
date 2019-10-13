#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 09:42:36 2019

@author: giudittaparolini
"""

#encapsulation, i.e protecting the properties of an object

class Student:
    def setId(self,iden):
        self.iden = iden
    
    def getId(self):
        return self.iden
    
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    

s = Student()
s.setId(123)
s.setName("John")
print(s.getId())
print(s.getName())
