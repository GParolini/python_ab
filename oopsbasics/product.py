#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 23:39:59 2019

@author: giudittaparolini
"""
#create a class
class Product:

    def __init__(self):
        self.name = "IPhone"
        self.description = "It's Awesome"
        self.price = 700

    def display(self):
        print(self.name)
        print(self.description)
        print(self.price)

p1 = Product()

print(p1.name)
print(p1.description)
print(p1.price)

p2 = Product()

print(p1.name)
print(p1.description)
print(p1.price)

print ("-----")

p1.display()
p2.display()
