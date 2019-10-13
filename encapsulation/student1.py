#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 09:42:36 2019

@author: giudittaparolini
"""

#encapsulation, i.e protecting the properties of an object

class Student:
    def __init__(self):
        #self.id = 123
        #self.name= "John"
        self.__id = 123 #private fields now that cannot be accessed utside of the class
        self.__name = "John"
        
    def display(self):
        print(self.__id)
        print(self.__name)

s = Student()

#print(s.id)
#print(s.name)

s.display()

print ("-------")

print(s._Student__id); #name mangling to get the private field
print(s._Student__name);